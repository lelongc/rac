/**
 * Form Generator - Dynamically create forms with validation
 */

// Store form fields configuration
let formFields = [];
let formConfig = {
    title: "",
    fields: []
};

// Initialize when document is ready
$(document).ready(function() {
    // Show/hide options field based on field type
    $('#fieldType').change(function() {
        const fieldType = $(this).val();
        if (fieldType === 'select' || fieldType === 'radio' || fieldType === 'checkbox') {
            $('#optionsContainer').show();
        } else {
            $('#optionsContainer').hide();
        }
    });
    
    // Add a new field to the form configuration
    $('#addFieldBtn').click(function() {
        addFieldToConfig();
    });
    
    // Clear all fields
    $('#clearFieldsBtn').click(function() {
        clearFields();
    });
    
    // Generate form preview
    $('#generateFormBtn').click(function() {
        generateFormPreview();
    });
    
    // Save form configuration to localStorage
    $('#saveFormBtn').click(function() {
        saveFormConfiguration();
    });
    
    // Load any saved forms
    loadSavedForms();
});

/**
 * Add a field to the form configuration
 */
function addFieldToConfig() {
    const label = $('#fieldLabel').val().trim();
    const type = $('#fieldType').val();
    const regex = $('#fieldRegex').val().trim();
    const errorMessage = $('#errorMessage').val().trim();
    const options = $('#fieldOptions').val().trim();
    
    if (!label) {
        alert('Please enter a field label');
        return;
    }
    
    // Create a field ID from the label
    const fieldId = label.toLowerCase().replace(/\s+/g, '_');
    
    // Create the field object
    const field = {
        id: fieldId,
        label: label,
        type: type,
        validation: regex,
        errorMessage: errorMessage || `Please enter a valid ${label.toLowerCase()}`,
        options: type === 'select' || type === 'radio' || type === 'checkbox' 
            ? options.split(',').map(opt => opt.trim())
            : []
    };
    
    // Add to form fields array
    formConfig.fields.push(field);
    
    // Update the fields list
    updateFieldsList();
    
    // Clear input fields
    $('#fieldLabel').val('');
    $('#fieldRegex').val('');
    $('#errorMessage').val('');
    $('#fieldOptions').val('');
}

/**
 * Update the list of fields in the UI
 */
function updateFieldsList() {
    if (formConfig.fields.length === 0) {
        $('#fieldsList').html('<p id="noFieldsMessage">No fields added yet.</p>');
        return;
    }
    
    let html = '';
    formConfig.fields.forEach((field, index) => {
        html += `
            <div class="field-row">
                <div class="d-flex justify-content-between">
                    <h5>${field.label}</h5>
                    <button class="btn btn-sm btn-danger delete-field" data-index="${index}">Remove</button>
                </div>
                <p><strong>Type:</strong> ${field.type}</p>
                ${field.validation ? `<p><strong>Validation:</strong> ${field.validation}</p>` : ''}
                ${field.errorMessage ? `<p><strong>Error Message:</strong> ${field.errorMessage}</p>` : ''}
                ${field.options && field.options.length > 0 ? 
                    `<p><strong>Options:</strong> ${field.options.join(', ')}</p>` : ''}
            </div>
        `;
    });
    
    $('#fieldsList').html(html);
    
    // Add event handlers for delete buttons
    $('.delete-field').click(function() {
        const index = $(this).data('index');
        formConfig.fields.splice(index, 1);
        updateFieldsList();
    });
}

/**
 * Clear all fields from the configuration
 */
function clearFields() {
    if (confirm('Are you sure you want to clear all fields?')) {
        formConfig.fields = [];
        updateFieldsList();
        $('#formPreview').html('<p>Form will appear here after generation.</p>');
    }
}

/**
 * Generate form preview
 */
function generateFormPreview() {
    formConfig.title = $('#formTitle').val() || 'Dynamic Form';
    
    if (formConfig.fields.length === 0) {
        alert('Please add at least one field to the form');
        return;
    }
    
    let formHtml = `
        <h3>${formConfig.title}</h3>
        <form id="dynamicForm" class="needs-validation" novalidate>
    `;
    
    formConfig.fields.forEach(field => {
        formHtml += `<div class="form-group">`;
        formHtml += `<label for="${field.id}">${field.label}</label>`;
        
        // Generate field based on type
        switch(field.type) {
            case 'text':
            case 'number':
            case 'email':
                formHtml += `
                    <input type="${field.type}" class="form-control" id="${field.id}" name="${field.id}" 
                        ${field.validation ? `data-validation="${field.validation}"` : ''}>
                    <div class="invalid-feedback" id="err_${field.id}">${field.errorMessage}</div>
                `;
                break;
                
            case 'date':
                formHtml += `
                    <input type="date" class="form-control" id="${field.id}" name="${field.id}" 
                        ${field.validation ? `data-validation="${field.validation}"` : ''}>
                    <div class="invalid-feedback" id="err_${field.id}">${field.errorMessage}</div>
                `;
                break;
                
            case 'select':
                formHtml += `<select class="form-control" id="${field.id}" name="${field.id}" 
                    ${field.validation ? `data-validation="${field.validation}"` : ''}>`;
                formHtml += `<option value="">-- Select ${field.label} --</option>`;
                field.options.forEach(option => {
                    formHtml += `<option value="${option}">${option}</option>`;
                });
                formHtml += `</select>
                    <div class="invalid-feedback" id="err_${field.id}">${field.errorMessage}</div>`;
                break;
                
            case 'radio':
                field.options.forEach((option, i) => {
                    formHtml += `
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="${field.id}" 
                                id="${field.id}_${i}" value="${option}" 
                                ${field.validation ? `data-validation="${field.validation}"` : ''}>
                            <label class="form-check-label" for="${field.id}_${i}">${option}</label>
                        </div>
                    `;
                });
                formHtml += `<div class="invalid-feedback" id="err_${field.id}">${field.errorMessage}</div>`;
                break;
                
            case 'checkbox':
                field.options.forEach((option, i) => {
                    formHtml += `
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" name="${field.id}[]" 
                                id="${field.id}_${i}" value="${option}" 
                                ${field.validation ? `data-validation="${field.validation}"` : ''}>
                            <label class="form-check-label" for="${field.id}_${i}">${option}</label>
                        </div>
                    `;
                });
                formHtml += `<div class="invalid-feedback" id="err_${field.id}">${field.errorMessage}</div>`;
                break;
        }
        
        formHtml += `</div>`;
    });
    
    formHtml += `
        <div class="form-group">
            <button type="submit" class="btn btn-primary">Submit</button>
        </div>
        </form>
        <div class="mt-4">
            <h4>Form Data:</h4>
            <pre id="formData" class="p-3 bg-light border">No data submitted yet</pre>
        </div>
    `;
    
    // Set the form HTML
    $('#formPreview').html(formHtml);
    
    // Add form validation and submission handler
    attachFormValidation();
}

/**
 * Attach validation to the generated form
 */
function attachFormValidation() {
    $('#dynamicForm').submit(function(event) {
        event.preventDefault();
        
        const formValid = validateForm();
        
        if (formValid) {
            const formData = {};
            const formArray = $(this).serializeArray();
            
            formArray.forEach(item => {
                if (formData[item.name]) {
                    if (Array.isArray(formData[item.name])) {
                        formData[item.name].push(item.value);
                    } else {
                        formData[item.name] = [formData[item.name], item.value];
                    }
                } else {
                    formData[item.name] = item.value;
                }
            });
            
            // Display form data
            $('#formData').text(JSON.stringify(formData, null, 2));
            
            // Generate table row
            generateTableRow(formData);
        }
    });
}

/**
 * Validate the form based on field configurations
 */
function validateForm() {
    let isValid = true;
    
    formConfig.fields.forEach(field => {
        const $field = $(`#${field.id}`);
        const value = $field.val();
        
        // Skip validation if no regex provided
        if (!field.validation) return;
        
        let fieldValid = true;
        
        switch(field.type) {
            case 'text':
            case 'number':
            case 'email':
            case 'date':
            case 'select':
                const regex = new RegExp(field.validation);
                fieldValid = regex.test(value);
                break;
                
            case 'radio':
                const radioChecked = $(`input[name='${field.id}']:checked`).length > 0;
                fieldValid = radioChecked;
                break;
                
            case 'checkbox':
                const checkboxChecked = $(`input[name='${field.id}[]']:checked`).length > 0;
                fieldValid = checkboxChecked;
                break;
        }
        
        if (!fieldValid) {
            $(`#err_${field.id}`).show();
            $field.addClass('is-invalid');
            isValid = false;
        } else {
            $(`#err_${field.id}`).hide();
            $field.removeClass('is-invalid');
        }
    });
    
    return isValid;
}

/**
 * Save form configuration to localStorage
 */
function saveFormConfiguration() {
    formConfig.title = $('#formTitle').val() || 'Dynamic Form';
    
    if (formConfig.fields.length === 0) {
        alert('Please add at least one field before saving');
        return;
    }
    
    // Generate a unique ID for this form configuration
    const formId = 'form_' + new Date().getTime();
    
    // Add to localStorage
    localStorage.setItem(formId, JSON.stringify(formConfig));
    
    alert('Form configuration saved successfully!');
    
    // Update saved forms list
    loadSavedForms();
}

/**
 * Load saved forms from localStorage
 */
function loadSavedForms() {
    const savedForms = [];
    
    // Iterate through localStorage items
    for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        
        // Check if this is a form config
        if (key.startsWith('form_')) {
            try {
                const formData = JSON.parse(localStorage.getItem(key));
                savedForms.push({
                    id: key,
                    title: formData.title,
                    fieldCount: formData.fields.length
                });
            } catch (e) {
                console.error('Error parsing saved form:', e);
            }
        }
    }
    
    // Display saved forms if any
    if (savedForms.length > 0) {
        let savedFormsHtml = `
            <div class="row mt-4">
                <div class="col-12">
                    <h3>Saved Forms</h3>
                    <div class="table-responsive">
                        <table class="table table-bordered">
                            <thead>
                                <tr>
                                    <th>Form Title</th>
                                    <th>Fields</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
        `;
        
        savedForms.forEach(form => {
            savedFormsHtml += `
                <tr>
                    <td>${form.title}</td>
                    <td>${form.fieldCount} fields</td>
                    <td>
                        <button class="btn btn-sm btn-info load-form" data-id="${form.id}">Load</button>
                        <button class="btn btn-sm btn-danger delete-form" data-id="${form.id}">Delete</button>
                        <a href="form-viewer.html?formId=${form.id}" class="btn btn-sm btn-success" target="_blank">View</a>
                    </td>
                </tr>
            `;
        });
        
        savedFormsHtml += `
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        `;
        
        // Add to page if saved forms section doesn't exist yet
        if ($('#savedForms').length === 0) {
            $('<div id="savedForms"></div>').insertAfter('.container > .row:last');
        }
        
        $('#savedForms').html(savedFormsHtml);
        
        // Add event handlers
        $('.load-form').click(function() {
            const formId = $(this).data('id');
            loadFormConfig(formId);
        });
        
        $('.delete-form').click(function() {
            const formId = $(this).data('id');
            
            if (confirm('Are you sure you want to delete this form?')) {
                localStorage.removeItem(formId);
                loadSavedForms();
            }
        });
    }
}

/**
 * Load a saved form configuration
 */
function loadFormConfig(formId) {
    try {
        const config = JSON.parse(localStorage.getItem(formId));
        
        if (!config) {
            alert('Form configuration not found');
            return;
        }
        
        formConfig = config;
        
        $('#formTitle').val(config.title);
        
        // Update fields list
        updateFieldsList();
        
        // Generate form preview
        generateFormPreview();
        
        alert('Form configuration loaded successfully!');
        
    } catch (e) {
        console.error('Error loading form configuration:', e);
        alert('Error loading form configuration');
    }
}

/**
 * Generate a table row with form data
 */
function generateTableRow(formData) {
    // Create table if it doesn't exist
    if ($('#dataTable').length === 0) {
        let tableHtml = `
            <div class="row mt-4">
                <div class="col-12">
                    <h3>Submitted Data</h3>
                    <div class="table-responsive">
                        <table id="dataTable" class="table table-bordered">
                            <thead>
                                <tr>
        `;
        
        // Add table headers based on form fields
        formConfig.fields.forEach(field => {
            tableHtml += `<th>${field.label}</th>`;
        });
        
        tableHtml += `
                                </tr>
                            </thead>
                            <tbody></tbody>
                        </table>
                    </div>
                </div>
            </div>
        `;
        
        $('#formPreview').append(tableHtml);
    }
    
    // Create row data
    let rowHtml = '<tr>';
    
    formConfig.fields.forEach(field => {
        let fieldValue = '';
        
        if (field.type === 'checkbox') {
            const values = formData[`${field.id}[]`];
            fieldValue = Array.isArray(values) ? values.join(', ') : values || '';
        } else {
            fieldValue = formData[field.id] || '';
        }
        
        rowHtml += `<td>${fieldValue}</td>`;
    });
    
    rowHtml += '</tr>';
    
    // Add to table
    $('#dataTable tbody').append(rowHtml);
}
