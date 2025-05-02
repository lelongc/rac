/**
 * Drag and Drop Logic for GFree English Course Web Builder
 * Enables dragging components from palette to canvas
 */

// Wrap all functionality in an IIFE to avoid polluting global scope
(function () {
  // Object to store the currently selected component
  const state = {
    selectedComponent: null,
    draggedComponentType: null,
  };

  // Initialize all drag and drop functionality
  function init() {
    console.log("Initializing drag and drop functionality");
    // Force re-initialization even if already setup
    setupDraggableComponents(true);
    setupDropZone();
    setupComponentSelection();
    setupExamplePreview();
  }

  /**
   * Make components in the palette draggable
   */
  function setupDraggableComponents(force = false) {
    const draggables = document.querySelectorAll(".draggable-component");
    console.log(`Found ${draggables.length} draggable components to setup`);

    draggables.forEach((draggable) => {
      // Skip if already initialized and not forcing
      if (!force && draggable.hasAttribute("data-draggable-initialized"))
        return;

      // Mark as initialized
      draggable.setAttribute("data-draggable-initialized", "true");

      // Make the element draggable
      draggable.setAttribute("draggable", "true");

      // Clean up any existing event listeners
      draggable.removeEventListener("dragstart", handleDragStart);
      draggable.removeEventListener("dragend", handleDragEnd);

      // Add event listeners for drag start
      draggable.addEventListener("dragstart", handleDragStart);
      draggable.addEventListener("dragend", handleDragEnd);

      console.log(`Set up draggable: ${draggable.textContent.trim()}`);
    });
  }

  /**
   * Set up the canvas area as a drop zone
   */
  function setupDropZone() {
    const dropZone = document.querySelector(".canvas-container");
    if (!dropZone) {
      console.error("Canvas container not found");
      return;
    }

    // Clean up existing listeners to prevent duplicates
    dropZone.removeEventListener("dragover", handleDragOver);
    dropZone.removeEventListener("dragenter", handleDragEnter);
    dropZone.removeEventListener("dragleave", handleDragLeave);
    dropZone.removeEventListener("drop", handleDrop);

    // Add event listeners for drop events
    dropZone.addEventListener("dragover", handleDragOver);
    dropZone.addEventListener("dragenter", handleDragEnter);
    dropZone.addEventListener("dragleave", handleDragLeave);
    dropZone.addEventListener("drop", handleDrop);

    console.log("Drop zone configured successfully");
  }

  /**
   * Set up event handlers for component selection in the canvas
   */
  function setupComponentSelection() {
    const canvas = document.querySelector(".canvas-container");
    if (!canvas) return;

    // Clean up existing listener
    canvas.removeEventListener("click", handleCanvasComponentClick);

    // Add new listener using named function for potential future cleanup
    canvas.addEventListener("click", handleCanvasComponentClick);

    // Add component interaction buttons event handling
    document.addEventListener("click", handleComponentButtons);
  }

  /**
   * Handle clicks on components in the canvas
   */
  function handleCanvasComponentClick(e) {
    // Check if we clicked on a component or one of its children
    const component = e.target.closest(".canvas-component");

    // Skip if clicked on action buttons
    if (e.target.closest(".component-actions")) return;

    if (component) {
      // Deselect any previously selected component
      const previouslySelected = document.querySelector(
        ".canvas-component.selected"
      );
      if (previouslySelected) {
        previouslySelected.classList.remove("selected");
      }

      // Select this component
      component.classList.add("selected");
      state.selectedComponent = component.id;

      // Show component properties in the right panel
      showComponentProperties(component.id);

      // Prevent the click from bubbling up to the canvas
      e.stopPropagation();
    } else {
      // Clicked on canvas but not on a component - deselect all
      deselectAllComponents();
    }
  }

  /**
   * Handle clicks on component action buttons
   */
  function handleComponentButtons(e) {
    // Handle move up button
    if (e.target.closest(".move-up")) {
      e.preventDefault();
      e.stopPropagation();

      const component = e.target.closest(".canvas-component");
      if (component) {
        moveComponent(component.id, "up");
      }
    }
    // Handle move down button
    else if (e.target.closest(".move-down")) {
      e.preventDefault();
      e.stopPropagation();

      const component = e.target.closest(".canvas-component");
      if (component) {
        moveComponent(component.id, "down");
      }
    }
    // Handle delete button
    else if (e.target.closest(".delete")) {
      e.preventDefault();
      e.stopPropagation();

      const component = e.target.closest(".canvas-component");
      if (component) {
        if (confirm("Are you sure you want to delete this component?")) {
          deleteComponent(component.id);
        }
      }
    }
  }

  /**
   * Move a component up or down
   */
  function moveComponent(componentId, direction) {
    const components = window.pageModelManager.getComponents();
    const index = components.findIndex((comp) => comp.id === componentId);

    // Skip if not found
    if (index === -1) return;

    let newIndex = index;
    if (direction === "up" && index > 0) {
      newIndex = index - 1;
    } else if (direction === "down" && index < components.length - 1) {
      newIndex = index + 1;
    } else {
      return; // No change needed
    }

    // Move the component
    window.pageModelManager.moveComponent(componentId, newIndex);

    // Notify about the model update
    notifyModelUpdated();

    console.log(
      `Moved component ${componentId} ${direction} to position ${newIndex}`
    );
  }

  /**
   * Delete a component from the model
   */
  function deleteComponent(componentId) {
    window.pageModelManager.removeComponent(componentId);

    // If this was the selected component, deselect it
    if (state.selectedComponent === componentId) {
      state.selectedComponent = null;

      // Hide properties panel
      document.querySelector(".no-selection-message").style.display = "block";
      document.querySelector(".component-properties").style.display = "none";
    }

    notifyModelUpdated();
    console.log(`Deleted component ${componentId}`);
  }

  /**
   * Set up example preview buttons
   */
  function setupExamplePreview() {
    // Add example template preview button
    const componentPalette = document.getElementById("component-palette");
    if (componentPalette) {
      // Add example website preview section
      const examplesCard = document.createElement("div");
      examplesCard.className = "card mt-3";
      examplesCard.innerHTML = `
        <div class="card-header bg-success text-white">
          <h5 class="mb-0">Example Templates</h5>
        </div>
        <div class="card-body">
          <div class="d-grid gap-2">
            <button class="btn btn-outline-primary" id="example-course-website">
              <i class="bi bi-file-earmark-code me-2"></i>English Course Site
            </button>
            <button class="btn btn-outline-primary" id="example-flower-website">
              <i class="bi bi-file-earmark-code me-2"></i>Flower Shop Site
            </button>
          </div>
        </div>
      `;

      // Add after instructions card
      const instructionsCard =
        componentPalette.querySelector(".card:nth-child(2)");
      if (instructionsCard) {
        instructionsCard.after(examplesCard);
      } else {
        componentPalette.appendChild(examplesCard);
      }

      // Add event listeners
      document
        .getElementById("example-course-website")
        ?.addEventListener("click", loadEnglishCourseTemplate);
      document
        .getElementById("example-flower-website")
        ?.addEventListener("click", loadFlowerShopTemplate);
    }
  }

  /**
   * Load English Course website template
   */
  function loadEnglishCourseTemplate() {
    if (
      !confirm(
        "This will replace your current design with the English Course template. Continue?"
      )
    )
      return;

    // Clear current components
    window.pageModelManager.clearComponents();

    // Add components for English course site template
    const header = window.pageModelManager.addComponent("header");
    header.logoUrl = "../image/website.png";

    const nav = window.pageModelManager.addComponent("nav");
    nav.orientation = "vertical";
    nav.items = [
      { text: "GFree English", url: "#" },
      { text: "Trang chủ", url: "#home" },
      { text: "Giới thiệu", url: "#about" },
      { text: "Khóa học", url: "#courses" },
      { text: "Web Builder", url: "../html/builder.html" },
    ];

    const tableComponent = window.pageModelManager.addComponent("table");
    tableComponent.title = "Danh sách đăng kí khóa học";

    const modalComponent = window.pageModelManager.addComponent("modal");

    const footer = window.pageModelManager.addComponent("footer");

    notifyModelUpdated();
    window.WebBuilder.showToast("English Course template loaded", "success");
  }

  /**
   * Load Flower Shop website template
   */
  function loadFlowerShopTemplate() {
    if (
      !confirm(
        "This will replace your current design with the Flower Shop template. Continue?"
      )
    )
      return;

    // Clear current components
    window.pageModelManager.clearComponents();

    // Add components for flower shop template
    const header = window.pageModelManager.addComponent("header");
    header.logoUrl = "../image/1.jpg";

    const nav = window.pageModelManager.addComponent("nav");
    nav.items = [
      { text: "Trang chủ", url: "#" },
      { text: "Sản phẩm", url: "#products" },
      { text: "Tin tức", url: "#news" },
      { text: "Liên hệ", url: "#contact" },
    ];
    nav.registerButtonText = "Đặt mua hoa";

    // Add image-table layout
    const imageTable =
      window.pageModelManager.addComponent("image-table-layout");
    imageTable.image.url = "../image/3.jpg";
    imageTable.table.title = "Danh Sách Thông Tin Đặt Hàng Nhanh";
    imageTable.table.columns = [
      { headerText: "STT" },
      { headerText: "Họ và tên" },
      { headerText: "Số điện thoại" },
      { headerText: "Ngày đặt" },
      { headerText: "Email" },
      { headerText: "Ảnh đại diện" },
    ];

    const modalComponent = window.pageModelManager.addComponent("modal");
    modalComponent.title = "Thông Tin Đặt Hàng";

    const footer = window.pageModelManager.addComponent("footer");

    notifyModelUpdated();
    window.WebBuilder.showToast("Flower Shop template loaded", "success");
  }

  // --- Drag Event Handlers ---

  /**
   * Handle the start of a drag operation
   */
  function handleDragStart(e) {
    console.log("Drag start");
    // Store the component type being dragged
    const componentType = this.getAttribute("data-component");
    state.draggedComponentType = componentType;

    // Set drag data - IMPORTANT: This must be set for Firefox to work properly
    e.dataTransfer.setData("text/plain", componentType);
    e.dataTransfer.effectAllowed = "copy";

    // Add visual feedback
    this.classList.add("dragging");
    document.body.style.cursor = "grabbing";
  }

  /**
   * Handle the end of a drag operation
   */
  function handleDragEnd(e) {
    console.log("Drag end");
    // Remove the dragging class
    this.classList.remove("dragging");
    state.draggedComponentType = null;
    document.body.style.cursor = "";
  }

  /**
   * Handle drag over event (required to allow dropping)
   */
  function handleDragOver(e) {
    // This is essential to allow dropping
    e.preventDefault();
    e.dataTransfer.dropEffect = "copy";
  }

  /**
   * Handle drag enter event for visual feedback
   */
  function handleDragEnter(e) {
    e.preventDefault();
    this.classList.add("highlight");

    // Hide the initial message when dragging over
    const dropzoneMessage = this.querySelector(".dropzone-message");
    if (dropzoneMessage) {
      dropzoneMessage.style.display = "none";
    }
  }

  /**
   * Handle drag leave event to remove visual feedback
   */
  function handleDragLeave(e) {
    // Only remove highlight if we're actually leaving the dropzone,
    // not just entering a child element
    const rect = this.getBoundingClientRect();
    const isStillInside =
      e.clientX >= rect.left &&
      e.clientX <= rect.right &&
      e.clientY >= rect.top &&
      e.clientY <= rect.bottom;

    if (!isStillInside) {
      this.classList.remove("highlight");

      // Show the message again if there are no components
      const dropzoneMessage = this.querySelector(".dropzone-message");
      if (
        dropzoneMessage &&
        window.pageModelManager.getComponents().length === 0
      ) {
        dropzoneMessage.style.display = "block";
      }
    }
  }

  /**
   * Handle drop event to add a new component to the canvas
   */
  function handleDrop(e) {
    e.preventDefault();
    e.stopPropagation();
    console.log("Drop event handled");

    // Remove highlight class
    this.classList.remove("highlight");

    try {
      // Get component type from data transfer
      const componentType = e.dataTransfer.getData("text/plain");

      if (!componentType) {
        console.error("No component type found in drop data");
        alert(
          "Error: Drag and drop failed. Please try again or reload the page."
        );
        return;
      }

      console.log("Adding component:", componentType);

      // Add the component to the model
      const newComponent = window.pageModelManager.addComponent(componentType);

      // Notify about model update
      notifyModelUpdated();

      // Select the newly added component
      setTimeout(() => selectNewComponent(newComponent.id), 100);
    } catch (error) {
      console.error("Error in drop handler:", error);
      alert("An error occurred while adding the component.");
    }
  }

  /**
   * Select a newly added component
   */
  function selectNewComponent(componentId) {
    const element = document.getElementById(componentId);
    if (element) {
      // Deselect any previously selected components
      const selected = document.querySelector(".canvas-component.selected");
      if (selected) selected.classList.remove("selected");

      // Select the new component
      element.classList.add("selected");
      state.selectedComponent = componentId;

      // Show properties
      showComponentProperties(componentId);

      // Scroll component into view
      element.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  }

  /**
   * Deselect all components in the canvas
   */
  function deselectAllComponents() {
    const selected = document.querySelector(".canvas-component.selected");
    if (selected) {
      selected.classList.remove("selected");
    }
    state.selectedComponent = null;

    // Hide the component properties in the right panel
    document.querySelector(".no-selection-message").style.display = "block";
    document.querySelector(".component-properties").style.display = "none";
  }

  /**
   * Show component properties in the right panel
   */
  function showComponentProperties(componentId) {
    document.dispatchEvent(
      new CustomEvent("componentSelected", {
        detail: { componentId },
      })
    );
  }

  /**
   * Notify that the model has been updated
   */
  function notifyModelUpdated() {
    document.dispatchEvent(new CustomEvent("modelUpdated"));
  }

  // Initialize when DOM is fully loaded
  function domReady() {
    init();

    // Check if draggable components were set up
    setTimeout(() => {
      const draggables = document.querySelectorAll(
        ".draggable-component[data-draggable-initialized]"
      );
      if (draggables.length === 0) {
        console.warn("No draggable components initialized. Trying again...");
        init();
      }
    }, 500);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", domReady);
  } else {
    domReady();
  }

  // Expose public API
  window.DragDropManager = {
    init,
    setupDraggableComponents,
    loadEnglishCourseTemplate,
    loadFlowerShopTemplate,
  };
})();
