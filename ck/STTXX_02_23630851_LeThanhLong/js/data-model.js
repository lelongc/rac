/**
 * Data Model Management for GFree English Course Web Builder
 * Manages the structure and state of the web page being built
 */

class PageModelManager {
  constructor() {
    // Array to store components in order of appearance
    this.components = [];
    // Generate a unique page ID
    this.pageId = "page_" + Date.now();
    // Page metadata
    this.metadata = {
      title: "New Page",
      description: "Created with GFree English Course Web Builder",
      author: "",
      createdAt: new Date().toISOString(),
      updatedAt: new Date().toISOString(),
    };
  }

  /**
   * Add a component to the page model
   * @param {string} componentType - The type of component to add
   * @returns {Object} The created component
   */
  addComponent(componentType) {
    try {
      console.log("Creating component of type:", componentType);
      const component = ComponentFactory.createComponent(componentType);
      console.log("Component created:", component);

      // Add the component to the components array
      this.components.push(component);
      return component;
    } catch (error) {
      console.error("Error creating component:", error);
      throw error;
    }
  }

  /**
   * Add a new component to the model
   * @param {string} componentType - Type of component to add (header, nav, table, etc.)
   * @param {number} position - Position to insert the component (0-based index)
   * @returns {Object} - The newly added component object
   */
  addComponent(componentType, position = null) {
    // Create a new component using the component factory
    const component =
      window.ComponentLibrary.ComponentFactory.createComponent(componentType);

    // If position is null or invalid, append to the end
    if (
      position === null ||
      position < 0 ||
      position > this.components.length
    ) {
      this.components.push(component);
    } else {
      // Insert at the specified position
      this.components.splice(position, 0, component);
    }

    this.updateMetadata();
    return component;
  }

  /**
   * Remove a component from the page model
   * @param {string} componentId - ID of the component to remove
   * @returns {boolean} Success flag
   */
  removeComponent(componentId) {
    const initialLength = this.components.length;
    this.components = this.components.filter((comp) => comp.id !== componentId);

    // Return true if a component was actually removed
    return initialLength > this.components.length;
  }

  /**
   * Update properties of a specific component
   * @param {string} componentId - ID of the component to update
   * @param {Object} properties - Key-value pairs of properties to update
   * @returns {boolean} - True if component was found and updated
   */
  updateComponent(componentId, properties) {
    const component = this.components.find((comp) => comp.id === componentId);

    if (!component) {
      return false;
    }

    // Update each property provided
    for (const [key, value] of Object.entries(properties)) {
      // Handle nested properties (like style.backgroundColor)
      if (key.includes(".")) {
        const [parent, child] = key.split(".");
        component[parent][child] = value;
      } else {
        component[key] = value;
      }
    }

    this.updateMetadata();
    return true;
  }

  /**
   * Get all components in the model
   * @returns {Array} - Array of all components
   */
  getComponents() {
    return [...this.components]; // Return a copy to prevent direct modification
  }

  /**
   * Get a specific component by ID
   * @param {string} componentId - ID of the component to find
   * @returns {Object|null} - The component object or null if not found
   */
  getComponentById(componentId) {
    return this.components.find((comp) => comp.id === componentId) || null;
  }

  /**
   * Move a component to a new position in the components array
   * @param {string} componentId - ID of the component to move
   * @param {number} newIndex - New position index for the component
   */
  moveComponent(componentId, newIndex) {
    if (newIndex < 0 || newIndex >= this.components.length) {
      console.error("Invalid new index for component movement:", newIndex);
      return false;
    }

    // Find the component's current index
    const currentIndex = this.components.findIndex(
      (comp) => comp.id === componentId
    );
    if (currentIndex === -1) {
      console.error("Component not found for movement:", componentId);
      return false;
    }

    // Don't do anything if it's already at the target position
    if (currentIndex === newIndex) {
      return true;
    }

    // Remove the component from its current position
    const [component] = this.components.splice(currentIndex, 1);

    // Insert it at the new position
    this.components.splice(newIndex, 0, component);

    return true;
  }

  /**
   * Load page model from JSON data
   * @param {string|Object} jsonData - JSON string or object to load
   * @returns {boolean} - True if model was successfully loaded
   */
  loadModel(jsonData) {
    try {
      // Parse JSON if it's a string
      const data =
        typeof jsonData === "string" ? JSON.parse(jsonData) : jsonData;

      if (!data || !Array.isArray(data.components)) {
        console.error("Invalid model data");
        return false;
      }

      // Clear existing components
      this.components = [];

      // Load metadata if available
      if (data.pageId) this.pageId = data.pageId;
      if (data.metadata) this.metadata = { ...this.metadata, ...data.metadata };

      // Recreate each component
      data.components.forEach((componentData) => {
        const component =
          window.ComponentLibrary.ComponentFactory.createComponent(
            componentData.type
          );

        // Copy all properties except type (which was used to create the component)
        for (const [key, value] of Object.entries(componentData)) {
          if (key !== "type") {
            component[key] = value;
          }
        }

        this.components.push(component);
      });

      return true;
    } catch (error) {
      console.error("Error loading model:", error);
      return false;
    }
  }

  /**
   * Save current model as JSON
   * @param {boolean} prettyPrint - Whether to format the JSON with indentation
   * @returns {string} - JSON string representation of the model
   */
  saveModel(prettyPrint = false) {
    this.updateMetadata();

    const modelData = {
      pageId: this.pageId,
      metadata: this.metadata,
      components: this.components,
    };

    // Convert to JSON string with optional pretty printing
    return JSON.stringify(modelData, null, prettyPrint ? 2 : 0);
  }

  /**
   * Update the metadata's lastUpdated timestamp
   * @private
   */
  updateMetadata() {
    this.metadata.updatedAt = new Date().toISOString();
  }

  /**
   * Set page title and other metadata
   * @param {Object} metadata - Object containing metadata properties
   */
  setMetadata(metadata) {
    this.metadata = { ...this.metadata, ...metadata };
    this.updateMetadata();
  }

  /**
   * Clear all components from the model
   */
  clearModel() {
    this.components = [];
    this.updateMetadata();
  }
}

// Create a singleton instance
window.pageModelManager = new PageModelManager();
