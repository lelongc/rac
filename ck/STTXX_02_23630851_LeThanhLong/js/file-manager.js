/**
 * File Manager Module for GFree English Course Web Builder
 * Handles saving, loading, and exporting functionality
 */

const FileManager = (function () {
  // Constants
  const STORAGE_KEY = "gfree-builder-model";

  /**
   * Save the current model to localStorage
   * @returns {boolean} Success status
   */
  function saveModelToStorage() {
    try {
      const modelJson = window.pageModelManager.saveModel();
      localStorage.setItem(STORAGE_KEY, modelJson);
      return true;
    } catch (error) {
      console.error("Error saving model to localStorage:", error);
      return false;
    }
  }

  /**
   * Load model from localStorage
   * @returns {boolean} Success status
   */
  function loadModelFromStorage() {
    try {
      const modelJson = localStorage.getItem(STORAGE_KEY);
      if (!modelJson) {
        console.warn("No saved model found in localStorage");
        return false;
      }

      const success = window.pageModelManager.loadModel(modelJson);
      if (success) {
        notifyModelUpdated();
        return true;
      }

      return false;
    } catch (error) {
      console.error("Error loading model from localStorage:", error);
      return false;
    }
  }

  /**
   * Export the current model as a downloadable JSON file
   */
  function exportModelAsJson() {
    try {
      const modelJson = window.pageModelManager.saveModel(true); // true for pretty-printing
      const filename = `gfree-website-${Date.now()}.json`;

      downloadFile(modelJson, filename, "application/json");
      return true;
    } catch (error) {
      console.error("Error exporting model as JSON:", error);
      return false;
    }
  }

  /**
   * Import model from a JSON file
   * @param {File} file - The JSON file to import
   * @returns {Promise<boolean>} Promise resolving to success status
   */
  function importModelFromJson(file) {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();

      reader.onload = function (e) {
        try {
          const jsonContent = e.target.result;
          const success = window.pageModelManager.loadModel(jsonContent);

          if (success) {
            notifyModelUpdated();
            resolve(true);
          } else {
            reject(new Error("Invalid model format"));
          }
        } catch (error) {
          console.error("Error importing model:", error);
          reject(error);
        }
      };

      reader.onerror = function () {
        reject(new Error("Error reading file"));
      };

      reader.readAsText(file);
    });
  }

  /**
   * Export the generated code as downloadable files
   * @param {boolean} asZip - Whether to export as ZIP file
   */
  function exportGeneratedCode(asZip = false) {
    try {
      const codeFiles = window.CodeGenerator.generateCode();

      if (asZip && typeof JSZip !== "undefined") {
        exportAsZip(codeFiles);
      } else {
        // Fall back to individual file downloads
        downloadFile(codeFiles.html, "index.html", "text/html");
        downloadFile(codeFiles.css, "style.css", "text/css");
        downloadFile(codeFiles.js, "script.js", "application/javascript");
      }

      return true;
    } catch (error) {
      console.error("Error exporting generated code:", error);
      return false;
    }
  }

  /**
   * Export files as a ZIP archive
   * @param {Object} codeFiles - Object containing HTML, CSS, and JS code
   */
  function exportAsZip(codeFiles) {
    const zip = new JSZip();

    // Add files to the ZIP
    zip.file("index.html", codeFiles.html);

    // Create css folder
    const cssFolder = zip.folder("css");
    cssFolder.file("style.css", codeFiles.css);
    cssFolder.file("bootstrap.min.css", "/* Include Bootstrap CSS here */");

    // Create js folder
    const jsFolder = zip.folder("js");
    jsFolder.file("script.js", codeFiles.js);
    jsFolder.file("jquery-3.7.1.min.js", "/* Include jQuery here */");
    jsFolder.file("bootstrap.bundle.min.js", "/* Include Bootstrap JS here */");

    // Create img folder
    const imgFolder = zip.folder("image");

    // Generate the ZIP file
    zip.generateAsync({ type: "blob" }).then(function (content) {
      downloadFile(content, "gfree-website.zip", "application/zip");
    });
  }

  /**
   * Show a preview of the generated code in a modal
   */
  function showCodePreview() {
    const codeFiles = window.CodeGenerator.generateCode();

    // Create or get modal
    let codeModal = document.getElementById("code-preview-modal");
    if (!codeModal) {
      codeModal = createCodePreviewModal();
      document.body.appendChild(codeModal);

      // Add event listener for download button
      document
        .getElementById("download-code-btn")
        .addEventListener("click", function () {
          exportGeneratedCode(true);
        });

      document
        .getElementById("download-json-btn")
        .addEventListener("click", function () {
          exportModelAsJson();
        });
    }

    // Update code content
    document.getElementById("html-code").textContent = codeFiles.html;
    document.getElementById("css-code").textContent = codeFiles.css;
    document.getElementById("js-code").textContent = codeFiles.js;

    // Show the modal
    const modal = new bootstrap.Modal(codeModal);
    modal.show();
  }

  /**
   * Create the code preview modal element
   * @returns {HTMLElement} The modal element
   */
  function createCodePreviewModal() {
    const modal = document.createElement("div");
    modal.id = "code-preview-modal";
    modal.className = "modal fade";
    modal.tabIndex = -1;
    modal.innerHTML = `
            <div class="modal-dialog modal-xl">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title">Generated Website Code</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body p-0">
                        <nav>
                            <div class="nav nav-tabs" id="code-tab" role="tablist">
                                <button class="nav-link active" id="html-tab" data-bs-toggle="tab" data-bs-target="#html" type="button" role="tab" aria-controls="html" aria-selected="true">HTML</button>
                                <button class="nav-link" id="css-tab" data-bs-toggle="tab" data-bs-target="#css" type="button" role="tab" aria-controls="css" aria-selected="false">CSS</button>
                                <button class="nav-link" id="js-tab" data-bs-toggle="tab" data-bs-target="#js" type="button" role="tab" aria-controls="js" aria-selected="false">JavaScript</button>
                            </div>
                        </nav>
                        <div class="tab-content" id="code-tab-content">
                            <div class="tab-pane fade show active" id="html" role="tabpanel" aria-labelledby="html-tab">
                                <pre class="m-0 p-3" style="max-height: 500px; overflow-y: auto;"><code id="html-code"></code></pre>
                            </div>
                            <div class="tab-pane fade" id="css" role="tabpanel" aria-labelledby="css-tab">
                                <pre class="m-0 p-3" style="max-height: 500px; overflow-y: auto;"><code id="css-code"></code></pre>
                            </div>
                            <div class="tab-pane fade" id="js" role="tabpanel" aria-labelledby="js-tab">
                                <pre class="m-0 p-3" style="max-height: 500px; overflow-y: auto;"><code id="js-code"></code></pre>
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-primary" id="download-code-btn">
                            <i class="bi bi-file-earmark-zip"></i> Download as ZIP
                        </button>
                        <button type="button" class="btn btn-outline-secondary" id="download-json-btn">
                            <i class="bi bi-file-earmark-code"></i> Download Model JSON
                        </button>
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    </div>
                </div>
            </div>
        `;
    return modal;
  }

  /**
   * Show the file import modal
   */
  function showImportModal() {
    // Create or get modal
    let importModal = document.getElementById("import-modal");
    if (!importModal) {
      importModal = document.createElement("div");
      importModal.id = "import-modal";
      importModal.className = "modal fade";
      importModal.tabIndex = -1;
      importModal.innerHTML = `
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">Import Website Model</h5>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>
                        <div class="modal-body">
                            <p>Upload a previously saved GFree website model JSON file.</p>
                            <div class="alert alert-warning">
                                <i class="bi bi-exclamation-triangle me-2"></i>
                                Importing a model will replace your current work.
                            </div>
                            <div class="mb-3">
                                <label for="import-file" class="form-label">Select JSON file</label>
                                <input class="form-control" type="file" id="import-file" accept=".json">
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-primary" id="import-btn" disabled>Import</button>
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                        </div>
                    </div>
                </div>
            `;
      document.body.appendChild(importModal);

      // Add event listeners for file selection and import button
      const fileInput = importModal.querySelector("#import-file");
      const importBtn = importModal.querySelector("#import-btn");

      fileInput.addEventListener("change", function () {
        importBtn.disabled = !this.files || this.files.length === 0;
      });

      importBtn.addEventListener("click", function () {
        const file = fileInput.files[0];
        if (!file) return;

        importModelFromJson(file)
          .then(() => {
            // Close modal on success
            const modal = bootstrap.Modal.getInstance(importModal);
            modal.hide();
            showToast("Model imported successfully", "success");
          })
          .catch((error) => {
            console.error("Import error:", error);
            showToast("Failed to import model", "danger");
          });
      });
    }

    // Reset the form
    const fileInput = importModal.querySelector("#import-file");
    fileInput.value = "";
    importModal.querySelector("#import-btn").disabled = true;

    // Show the modal
    const modal = new bootstrap.Modal(importModal);
    modal.show();
  }

  /**
   * Create and show a toast notification
   * @param {string} message - The message to show
   * @param {string} type - The type of toast (success, danger, etc.)
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

    // Create the toast
    const toastId = "toast-" + Date.now();
    const toast = document.createElement("div");
    toast.id = toastId;
    toast.className =
      `toast bg-${type} text-white` + (type === "light" ? " text-dark" : "");
    toast.setAttribute("role", "alert");
    toast.setAttribute("aria-live", "assertive");
    toast.setAttribute("aria-atomic", "true");

    toast.innerHTML = `
            <div class="toast-header bg-${type}" style="color: ${
      type === "light" ? "#000" : "#fff"
    }">
                <strong class="me-auto">GFree Web Builder</strong>
                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
            </div>
            <div class="toast-body">
                ${message}
            </div>
        `;

    toastContainer.appendChild(toast);

    // Show the toast
    const bsToast = new bootstrap.Toast(toast, {
      autohide: true,
      delay: 3000,
    });
    bsToast.show();

    // Remove toast from DOM after it's hidden
    toast.addEventListener("hidden.bs.toast", function () {
      toast.remove();
    });
  }

  /**
   * Download a file
   * @param {Blob|string} content - The file content
   * @param {string} filename - The file name
   * @param {string} mimeType - The MIME type
   */
  function downloadFile(content, filename, mimeType) {
    // Create a blob if content is a string
    const blob =
      typeof content === "string"
        ? new Blob([content], { type: mimeType })
        : content;

    // Create download link
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = filename;

    // Append to body, click and remove
    document.body.appendChild(link);
    link.click();

    // Clean up
    setTimeout(() => {
      URL.revokeObjectURL(link.href);
      document.body.removeChild(link);
    }, 100);
  }

  /**
   * Notify that the model has been updated
   */
  function notifyModelUpdated() {
    document.dispatchEvent(new CustomEvent("modelUpdated"));
  }

  /**
   * Create a toolbar with additional functionality
   */
  function createFileToolbar() {
    // Find the header toolbar
    const toolbar = document.querySelector(".row.bg-dark .col-auto");
    if (!toolbar) return;

    // Add an import button
    const importBtn = document.createElement("button");
    importBtn.className = "btn btn-sm btn-outline-info me-2";
    importBtn.innerHTML = '<i class="bi bi-folder-plus"></i> Import';
    importBtn.addEventListener("click", showImportModal);

    // Insert the import button before the preview button
    toolbar.insertBefore(importBtn, toolbar.firstChild);
  }

  /**
   * Setup event listeners for the save and preview buttons
   */
  function setupButtonHandlers() {
    // Find the save button
    const saveBtn = document.querySelector("button:has(.bi-save)");
    if (saveBtn) {
      saveBtn.addEventListener("click", function () {
        const success = saveModelToStorage();
        if (success) {
          showToast("Website saved to browser storage", "success");
        } else {
          showToast("Failed to save website", "danger");
        }
      });
    }

    // Find the preview button
    const previewBtn = document.querySelector("button:has(.bi-play-fill)");
    if (previewBtn) {
      previewBtn.addEventListener("click", showCodePreview);
    }
  }

  /**
   * Initialize the file manager
   */
  function init() {
    createFileToolbar();
    setupButtonHandlers();

    // Attempt to load saved model on startup
    setTimeout(() => {
      if (
        window.pageModelManager &&
        window.pageModelManager.getComponents().length === 0
      ) {
        loadModelFromStorage();
      }
    }, 500);
  }

  // Initialize when DOM is fully loaded
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  // Return public API
  return {
    saveModelToStorage,
    loadModelFromStorage,
    exportModelAsJson,
    importModelFromJson,
    exportGeneratedCode,
    showCodePreview,
    showImportModal,
  };
})();
