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
   * Remove a component from the model by its ID
   * @param {string} componentId - ID of the component to remove
   * @returns {boolean} - True if component was found and removed
   */
  removeComponent(componentId) {
    const initialLength = this.components.length;
    this.components = this.components.filter(
      (component) => component.id !== componentId
    );

    // Check if a component was actually removed
    const wasRemoved = initialLength > this.components.length;

    if (wasRemoved) {
      this.updateMetadata();
    }

    return wasRemoved;
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
   * Move a component to a new position
   * @param {string} componentId - ID of component to move
   * @param {number} newPosition - New position index
   * @returns {boolean} - True if move was successful
   */
  moveComponent(componentId, newPosition) {
    // Find the component's current index
    const currentIndex = this.components.findIndex(
      (comp) => comp.id === componentId
    );

    // Check if component exists and new position is valid
    if (
      currentIndex === -1 ||
      newPosition < 0 ||
      newPosition >= this.components.length
    ) {
      return false;
    }

    // Remove from current position
    const [component] = this.components.splice(currentIndex, 1);

    // Insert at new position
    this.components.splice(newPosition, 0, component);

    this.updateMetadata();
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
