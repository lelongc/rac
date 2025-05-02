/**
 * Main Application Module for GFree English Course Web Builder
 * Connects all modules and initializes the application
 */

const WebBuilder = (function () {
  // Application state
  const state = {
    initialized: false,
    selectedComponentId: null,
    dragging: false,
  };

  // DOM elements cache
  const elements = {
    canvas: null,
    componentPalette: null,
    propertiesPanel: null,
    exportButton: null,
    saveButton: null,
    loadButton: null,
    fullscreenButton: null,
  };

  /**
   * Initialize the application
   */
  function init() {
    if (state.initialized) return;

    // Cache DOM elements
    cacheElements();

    // Initialize the page model manager
    initializePageModel();

    // Set up drag-drop functionality
    initializeDragDrop();

    // Set up event listeners
    setupEventListeners();

    // Setup UI controls
    setupUIControls();

    // Try to load last saved model from storage
    loadLastSavedModel();

    // Mark as initialized
    state.initialized = true;

    console.log("Web Builder successfully initialized");
  }

  /**
   * Cache DOM elements for faster access
   */
  function cacheElements() {
    elements.canvas = document.querySelector(".canvas-container");
    elements.componentPalette = document.getElementById("component-palette");
    elements.propertiesPanel = document.getElementById("properties-panel");
    elements.exportButton = document.querySelector("button:has(.bi-play-fill)");
    elements.saveButton = document.querySelector("button:has(.bi-save)");
    elements.fullscreenButton = document.querySelector(
      "button:has(.bi-arrows-fullscreen)"
    );
  }

  /**
   * Initialize the page model manager
   */
  function initializePageModel() {
    // Create a new page model manager if it doesn't exist
    if (!window.pageModelManager) {
      window.pageModelManager = new PageModelManager();
    }

    // Initialize with default metadata
    window.pageModelManager.metadata = {
      title: "GFree English Course",
      description: "Learn English with GFree",
      author: "Lê Thanh Long",
    };
  }

  /**
   * Initialize drag-drop functionality
   */
  function initializeDragDrop() {
    // Make sure the drag-drop module exists
    if (!window.DragDropManager) {
      console.error("DragDropManager not found");
      return;
    }

    // Initialize drag-drop with the canvas
    DragDropManager.init(elements.canvas);
  }

  /**
   * Set up event listeners
   */
  function setupEventListeners() {
    // Listen for component selection events
    document.addEventListener("componentSelected", handleComponentSelected);

    // Listen for model updates
    document.addEventListener("modelUpdated", handleModelUpdated);

    // Listen for drag start/end events
    document.addEventListener("dragstart", () => {
      state.dragging = true;
    });
    document.addEventListener("dragend", () => {
      state.dragging = false;
    });

    // Listen for canvas clicks (for component selection)
    elements.canvas.addEventListener("click", handleCanvasClick);

    // Listen for keyboard events (like delete)
    document.addEventListener("keydown", handleKeyDown);
  }

  /**
   * Set up UI controls (buttons, etc.)
   */
  function setupUIControls() {
    // Export button (Preview)
    if (elements.exportButton) {
      elements.exportButton.addEventListener("click", exportCode);
    }

    // Save button
    if (elements.saveButton) {
      elements.saveButton.addEventListener("click", saveModel);
    }

    // Fullscreen button for canvas
    if (elements.fullscreenButton) {
      elements.fullscreenButton.addEventListener("click", toggleFullscreen);
    }
  }

  /**
   * Handle component selection event
   */
  function handleComponentSelected(e) {
    state.selectedComponentId = e.detail.componentId;
  }

  /**
   * Handle model updated event
   */
  function handleModelUpdated() {
    // Render the updated model
    if (typeof window.Renderer !== "undefined" && window.Renderer.render) {
      window.Renderer.render();
    }
  }

  /**
   * Handle clicks on the canvas for component selection
   */
  function handleCanvasClick(e) {
    // Don't handle clicks during drag operations
    if (state.dragging) return;

    // Find the closest component
    const componentElement = e.target.closest(".canvas-component");
    if (!componentElement) {
      // Clicked on empty canvas, deselect
      selectComponent(null);
      return;
    }

    // Get the component ID
    const componentId = componentElement.id;

    // Select the component
    selectComponent(componentId);
  }

  /**
   * Handle keyboard events
   */
  function handleKeyDown(e) {
    // Delete selected component with Delete key
    if (e.key === "Delete" && state.selectedComponentId) {
      const activeElement = document.activeElement;
      const isInputActive =
        activeElement.tagName === "INPUT" ||
        activeElement.tagName === "TEXTAREA" ||
        activeElement.tagName === "SELECT";

      // Only proceed if not focused on an input field
      if (!isInputActive) {
        deleteSelectedComponent();
      }
    }
  }

  /**
   * Select a component
   */
  function selectComponent(componentId) {
    // Update state
    state.selectedComponentId = componentId;

    // Notify about selection
    document.dispatchEvent(
      new CustomEvent("componentSelected", {
        detail: { componentId },
      })
    );

    // Update visual selection in the UI
    updateSelectionUI(componentId);
  }

  /**
   * Update UI to reflect the current selection
   */
  function updateSelectionUI(componentId) {
    // Remove selection from all components
    document.querySelectorAll(".canvas-component").forEach((el) => {
      el.classList.remove("selected");
    });

    // Add selection to selected component
    if (componentId) {
      const componentElement = document.getElementById(componentId);
      if (componentElement) {
        componentElement.classList.add("selected");
      }
    }
  }

  /**
   * Delete the currently selected component
   */
  function deleteSelectedComponent() {
    if (!state.selectedComponentId) return;

    // Confirm deletion
    if (confirm("Are you sure you want to delete this component?")) {
      // Remove from model
      window.pageModelManager.removeComponent(state.selectedComponentId);

      // Clear selection
      state.selectedComponentId = null;

      // Notify about model update
      document.dispatchEvent(new CustomEvent("modelUpdated"));
    }
  }

  /**
   * Toggle fullscreen mode for the canvas
   */
  function toggleFullscreen() {
    const canvasCard = elements.canvas.closest(".card");
    if (!canvasCard) return;

    canvasCard.classList.toggle("fullscreen-canvas");

    // Update the button icon
    if (elements.fullscreenButton) {
      const icon = elements.fullscreenButton.querySelector("i");
      if (icon) {
        if (canvasCard.classList.contains("fullscreen-canvas")) {
          icon.classList.remove("bi-arrows-fullscreen");
          icon.classList.add("bi-fullscreen-exit");
        } else {
          icon.classList.add("bi-arrows-fullscreen");
          icon.classList.remove("bi-fullscreen-exit");
        }
      }
    }
  }

  /**
   * Export the generated code
   */
  function exportCode() {
    // Use the CodeGenerator and FileManager to export code
    if (
      typeof window.CodeGenerator !== "undefined" &&
      window.CodeGenerator.showGeneratedCode
    ) {
      window.CodeGenerator.showGeneratedCode();
    } else if (
      typeof window.FileManager !== "undefined" &&
      window.FileManager.showCodePreview
    ) {
      window.FileManager.showCodePreview();
    }
  }

  /**
   * Save the current model
   */
  function saveModel() {
    // Use the FileManager to save the model
    if (
      typeof window.FileManager !== "undefined" &&
      window.FileManager.saveModelToStorage
    ) {
      const success = window.FileManager.saveModelToStorage();

      // Show feedback
      if (success) {
        showToast("Website saved successfully", "success");
      } else {
        showToast("Failed to save website", "danger");
      }
    } else {
      // Fallback to basic localStorage saving
      try {
        const modelJson = window.pageModelManager.saveModel();
        localStorage.setItem("gfree-builder-model", modelJson);
        showToast("Website saved successfully", "success");
      } catch (error) {
        console.error("Error saving model:", error);
        showToast("Failed to save website", "danger");
      }
    }
  }

  /**
   * Load the last saved model
   */
  function loadLastSavedModel() {
    // Use the FileManager to load the model
    if (
      typeof window.FileManager !== "undefined" &&
      window.FileManager.loadModelFromStorage
    ) {
      window.FileManager.loadModelFromStorage();
    } else {
      // Fallback to basic localStorage loading
      try {
        const modelJson = localStorage.getItem("gfree-builder-model");
        if (modelJson) {
          const success = window.pageModelManager.loadModel(modelJson);
          if (success) {
            // Notify about model update
            document.dispatchEvent(new CustomEvent("modelUpdated"));
          }
        }
      } catch (error) {
        console.error("Error loading model:", error);
      }
    }
  }

  /**
   * Show a toast notification
   */
  function showToast(message, type = "info") {
    // Create toast container if it doesn't exist
    let toastContainer = document.getElementById("toast-container");
    if (!toastContainer) {
      toastContainer = document.createElement("div");
      toastContainer.id = "toast-container";
      toastContainer.className =
        "toast-container position-fixed bottom-0 end-0 p-3";
      document.body.appendChild(toastContainer);
    }

    // Create and show toast
    const toastId = "toast-" + Date.now();
    const toast = document.createElement("div");
    toast.id = toastId;
    toast.className = `toast bg-${type} text-white`;
    toast.setAttribute("role", "alert");
    toast.setAttribute("aria-live", "assertive");
    toast.setAttribute("aria-atomic", "true");

    toast.innerHTML = `
            <div class="toast-header bg-${type} text-white">
                <strong class="me-auto">GFree Web Builder</strong>
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
            <div class="toast-body">
                ${message}
            </div>
        `;

    toastContainer.appendChild(toast);

    // Show the toast using Bootstrap
    const bsToast = new bootstrap.Toast(toast, {
      autohide: true,
      delay: 3000,
    });
    bsToast.show();
  }

  /**
   * Add a component to the model
   */
  function addComponent(type) {
    // Create a new component and add it to the model
    const component = window.pageModelManager.addComponent(type);

    // Notify about model update
    document.dispatchEvent(new CustomEvent("modelUpdated"));

    return component;
  }

  /**
   * Move a component up or down in the page
   */
  function moveComponent(componentId, direction) {
    if (!componentId) return;

    // Get component from model
    const components = window.pageModelManager.getComponents();
    const index = components.findIndex((c) => c.id === componentId);
    if (index === -1) return;

    // Calculate new index
    let newIndex;
    if (direction === "up") {
      newIndex = Math.max(0, index - 1);
    } else if (direction === "down") {
      newIndex = Math.min(components.length - 1, index + 1);
    } else {
      return;
    }

    // Move the component
    if (newIndex !== index) {
      window.pageModelManager.moveComponent(componentId, newIndex);

      // Notify about model update
      document.dispatchEvent(new CustomEvent("modelUpdated"));
    }
  }

  /**
   * Create new project/reset the builder
   */
  function createNewProject() {
    if (
      confirm(
        "Are you sure you want to create a new project? All unsaved changes will be lost."
      )
    ) {
      // Clear the model
      window.pageModelManager.clearComponents();

      // Notify about model update
      document.dispatchEvent(new CustomEvent("modelUpdated"));

      // Show notification
      showToast("New project created", "success");
    }
  }

  // Initialize when DOM is fully loaded
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  // Public API
  return {
    init,
    selectComponent,
    addComponent,
    deleteSelectedComponent,
    moveComponent,
    exportCode,
    saveModel,
    loadLastSavedModel,
    createNewProject,
    showToast,
  };
})();

// Make available globally
window.WebBuilder = WebBuilder;
