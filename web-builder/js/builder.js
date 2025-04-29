/**
 * Web Builder - Main functionality
 */

// Global variables
let selectedComponent = null;

$(document).ready(function() {
    initDragAndDrop();
    initComponentSelection();
    initPreview();
    initExport();
    updateModalPreviewCard();
});

/**
 * Initialize drag and drop functionality
 */
function initDragAndDrop() {
    // Make component items draggable
    $('.component-item').on('dragstart', function(e) {
        const componentType = $(this).data('type');
        e.originalEvent.dataTransfer.setData('component-type', componentType);
        e.originalEvent.dataTransfer.effectAllowed = 'copy';
    });

    // Make canvas a drop target
    const canvas = document.getElementById('canvas');
    
    canvas.addEventListener('dragover', function(e) {
        e.preventDefault();
        e.dataTransfer.dropEffect = 'copy';
        $(this).addClass('drag-over');
    });
    
    canvas.addEventListener('dragleave', function(e) {
        $(this).removeClass('drag-over');
    });
    
    canvas.addEventListener('drop', function(e) {
        e.preventDefault();
        $(this).removeClass('drag-over');
        
        const componentType = e.dataTransfer.getData('component-type');
        if (componentType) {
            // Clear placeholder if this is the first component
            if ($('#canvas .drop-placeholder').length > 0) {
                $('#canvas .drop-placeholder').remove();
            }
            
            // Add component to canvas
            addComponentToCanvas(componentType);
        }
    });

    // Make components sortable within canvas
    $('#canvas').sortable({
        handle: '.drag-handle',
        placeholder: 'ui-sortable-placeholder',
        forcePlaceholderSize: true,
        update: function(event, ui) {
            // Update component positions
            updateComponentOrder();
        }
    });
}

/**
 * Add a component to the canvas
 */
function addComponentToCanvas(componentType) {
    const componentId = 'component-' + Date.now();
    let component;
    
    // Create component based on type
    switch (componentType) {
        case 'banner':
            component = createBannerComponent(componentId);
            break;
        case 'navbar':
            component = createNavbarComponent(componentId);
            break;
        case 'table':
            component = createTableComponent(componentId);
            break;
        case 'text-field':
            component = createTextFieldComponent(componentId);
            break;
        case 'email-field':
            component = createEmailFieldComponent(componentId);
            break;
        case 'date-field':
            component = createDateFieldComponent(componentId);
            break;
        case 'select':
            component = createSelectComponent(componentId);
            break;
        case 'radio-group':
            component = createRadioGroupComponent(componentId);
            break;
        case 'checkbox-group':
            component = createCheckboxGroupComponent(componentId);
            break;
        case 'modal':
            component = createModalComponent(componentId);
            break;
        case 'button':
            component = createButtonComponent(componentId);
            break;
        case 'footer':
            component = createFooterComponent(componentId);
            break;
        default:
            console.error('Unknown component type:', componentType);
            return;
    }
    
    // Add component to canvas
    $('#canvas').append(component);
    
    // Update modal preview card visibility
    updateModalPreviewCard();
    
    // Select the newly added component
    selectComponent($('#' + componentId));
}

/**
 * Initialize component selection handling
 */
function initComponentSelection() {
    // Handle component selection
    $(document).on('click', '.canvas-component', function(e) {
        // Don't select if clicking on a button inside the component actions
        if ($(e.target).closest('.component-actions').length) {
            return;
        }
        
        selectComponent($(this));
        e.stopPropagation();
    });
    
    // Deselect when clicking elsewhere
    $(document).on('click', function(e) {
        if (!$(e.target).closest('.canvas-component, #properties-panel').length) {
            deselectComponents();
        }
    });
    
    // Component action buttons
    $(document).on('click', '.move-up-btn', function(e) {
        const component = $(this).closest('.canvas-component');
        const prev = component.prev('.canvas-component');
        if (prev.length) {
            component.insertBefore(prev);
            updateComponentOrder();
        }
        e.stopPropagation();
    });
    
    $(document).on('click', '.move-down-btn', function(e) {
        const component = $(this).closest('.canvas-component');
        const next = component.next('.canvas-component');
        if (next.length) {
            component.insertAfter(next);
            updateComponentOrder();
        }
        e.stopPropagation();
    });
    
    $(document).on('click', '.duplicate-btn', function(e) {
        const component = $(this).closest('.canvas-component');
        const componentType = component.data('type');
        const newComponentId = 'component-' + Date.now();
        
        // Clone the component
        let newComponent = component.clone(true);
        newComponent.attr('id', newComponentId);
        
        // Insert after the original
        component.after(newComponent);
        
        // Select the new component
        selectComponent(newComponent);
        updateComponentOrder();
        e.stopPropagation();
    });
    
    $(document).on('click', '.delete-btn', function(e) {
        const component = $(this).closest('.canvas-component');
        
        // If selected, clear properties panel
        if (component.hasClass('selected')) {
            $('#properties-panel').html(`
                <p class="text-center text-muted">
                    Select a component to edit its properties
                </p>
            `);
        }
        
        // Remove the component
        component.remove();
        
        // Update modal preview card visibility
        updateModalPreviewCard();
        
        // Add placeholder if canvas is now empty
        if ($('#canvas .canvas-component').length === 0) {
            $('#canvas').html(`
                <div class="drop-placeholder">
                    <i class="fas fa-arrow-down"></i>
                    <p>Drag components here</p>
                </div>
            `);
        }
        
        updateComponentOrder();
        e.stopPropagation();
    });

    // Modal edit button handler
    $(document).on('click', '.edit-modal-btn', function(e) {
        e.stopPropagation();
        const component = $(this).closest('.canvas-component');
        selectComponent(component);
        
        // Open a modal to edit fields if needed
        // This is already handled by showing the properties panel
    });
}

/**
 * Select a component for editing
 */
function selectComponent(component) {
    // Deselect any currently selected component
    deselectComponents();
    
    // Mark as selected
    component.addClass('selected');
    selectedComponent = component;
    
    // Show properties for the selected component
    const componentType = component.data('type');
    showComponentProperties(component, componentType);
}

/**
 * Deselect all components
 */
function deselectComponents() {
    $('.canvas-component').removeClass('selected');
    selectedComponent = null;
}

/**
 * Update component order after sorting
 */
function updateComponentOrder() {
    // Regenerate preview
    if ($('#preview-modal').hasClass('show')) {
        generatePreview();
    }
}

/**
 * Initialize preview functionality
 */
function initPreview() {
    $('#preview-btn').on('click', function() {
        generatePreview();
        $('#preview-modal').modal('show');
    });
    
    // Modal preview functionality
    $('#preview-modal-btn').on('click', function() {
        const modalComponent = $('#canvas .canvas-component[data-type="modal"]');
        
        if (modalComponent.length) {
            // Get modal ID
            const modalId = modalComponent.data('modal-id') || $('#modal-id').val() || 'myModal';
            
            // Find preview frame and get its document
            const previewFrame = document.getElementById('preview-frame');
            if (previewFrame && previewFrame.contentWindow) {
                const frameDocument = previewFrame.contentWindow.document;
                // Try to find and show the modal
                try {
                    frameDocument.getElementById(modalId).classList.add('show');
                    frameDocument.getElementById(modalId).style.display = 'block';
                    frameDocument.body.classList.add('modal-open');
                    frameDocument.body.insertAdjacentHTML('beforeend', '<div class="modal-backdrop fade show"></div>');
                } catch (e) {
                    alert('Modal not found in preview. Make sure you have a modal component added.');
                    console.error(e);
                }
            } else {
                alert('Please generate a preview first by clicking the Preview button.');
            }
        } else {
            alert('No modal component found. Please add a modal component to the canvas.');
        }
    });
}

/**
 * Show or hide the modal preview card based on whether a modal exists in the canvas
 */
function updateModalPreviewCard() {
    const hasModal = $('#canvas .canvas-component[data-type="modal"]').length > 0;
    
    if (hasModal) {
        $('#modal-preview-card').show();
    } else {
        $('#modal-preview-card').hide();
    }
}

/**
 * Generate preview of the current page
 */
function generatePreview() {
    const previewFrame = document.getElementById('preview-frame');
    const htmlCode = generateHTMLCode(true);
    
    // Set iframe content
    previewFrame.srcdoc = htmlCode;
}

/**
 * Initialize export functionality
 */
function initExport() {
    $('#export-btn').on('click', function() {
        // Generate code
        const htmlCode = generateHTMLCode(false);
        const jsCode = generateJSCode();
        const cssCode = generateCSSCode();
        
        // Set code in the export modal
        $('#html-code').text(htmlCode);
        $('#js-code').text(jsCode);
        $('#css-code').text(cssCode);
        
        // Show the export modal
        $('#export-modal').modal('show');
    });
    
    // Copy button functionality
    $('.copy-btn').click(function() {
        const targetId = $(this).data('target');
        const content = $('#' + targetId).text();
        
        // Copy to clipboard
        navigator.clipboard.writeText(content)
            .then(() => {
                // Show copied feedback
                const originalText = $(this).html();
                $(this).html('<i class="fas fa-check"></i> Copied!');
                setTimeout(() => {
                    $(this).html(originalText);
                }, 2000);
            })
            .catch(err => {
                console.error('Failed to copy: ', err);
            });
    });
}
