/**
 * Form Viewer - View and submit forms based on saved configuration
 */

let formConfig = null;
let submittedData = [];
const formDataKey = 'form_data_';

// Initialize when document is ready
$(document).ready(function() {
    // Get formId from URL
    const urlParams = new URLSearchParams(window.location.search);
    const formId = urlParams.get('formId');
    
    if (!formId) {
        showError('No form ID provided. Please return to the Form Generator.');
        return;
    }
    
    // Load form configuration
    loadFormConfig(formId);
    
    // Clear data button
    $('#clearDataBtn').click(function() {
        if (confirm('Are you sure you want to clear all submitted data?')) {
            localStorage.removeItem(formDataKey + formId);
            loadSubmittedData(formId);
        }
    });
});

/**
 * Show an error message
 */
function showError(message) {
    $('#formTitle').text('Error');
    $('#formContainer').html(`<div class="alert alert-danger">${message}</div>`);
}

/**
 * Load form configuration from localStorage
 */
function loadFormConfig(formId) {
    try {
        const configString = localStorage.getItem(formId);
        
        if (!configString) {
            showError('Form configuration not found');
            return;
        }
        
        formConfig = JSON.parse(configString);
        
        // Set form title
        $('#formTitle').text(formConfig.title);
        
        // Generate form
        generateForm(formId);
        
        // Load submitted data
        loadSubmittedData(formId);
        
    } catch (e) {
        console.error('Error loading form configuration:', e);
        showError('Error loading form configuration');
    }
}

/**
 * Generate form based on configuration
 */
function generateForm(formId) {
    if (!formConfig || !formConfig.fields || formConfig.fields.length === 0) {
        showError('Invalid form configuration');
        return;
    }
    
    let formHtml = `
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
    `;
    
    // Set the form HTML
    $('#formContainer').html(formHtml);
    
    // Setup table headers
    setupTableHeaders();
    
    // Add form validation and submission handler
    $('#dynamicForm').submit(function(event) {
        event.preventDefault();
        
        const formValid = validateForm();
        
        if (formValid) {
            submitForm(formId);
        }
    });
}

/**
 * Setup table headers based on form fields
 */
function setupTableHeaders() {
    if (!formConfig || !formConfig.fields) return;
    
    // Clear existing headers (except the first one which is #)
    $('#tableHeaders th:not(:first-child)').remove();
    
    // Add headers for each field
    formConfig.fields.forEach(field => {
        $('#tableHeaders').append(`<th>${field.label}</th>`);
    });
    
    // Add timestamp column
    $('#tableHeaders').append(`<th>Submitted</th>`);
}

/**
 * Validate the form based on field configurations
 */
function validateForm() {
    let isValid = true;
    
    formConfig.fields.forEach(field => {
        let fieldValid = true;
        
        // Different validation based on field type
        switch(field.type) {
            case 'text':
            case 'number':
            case 'email':
            case 'date':
            case 'select':
                const $field = $(`#${field.id}`);
                const value = $field.val();
                
                // Skip validation if no regex provided
                if (!field.validation) break;
                
                const regex = new RegExp(field.validation);
                fieldValid = regex.test(value);
                
                if (!fieldValid) {
                    $(`#err_${field.id}`).show();
                    $field.addClass('is-invalid');
                } else {
                    $(`#err_${field.id}`).hide();
                    $field.removeClass('is-invalid');
                }
                break;
                
            case 'radio':
                const radioChecked = $(`input[name='${field.id}']:checked`).length > 0;
                fieldValid = radioChecked;
                
                if (!fieldValid) {
                    $(`#err_${field.id}`).show();
                } else {
                    $(`#err_${field.id}`).hide();
                }
                break;
                
            case 'checkbox':
                const checkboxChecked = $(`input[name='${field.id}[]']:checked`).length > 0;
                fieldValid = checkboxChecked;
                
                if (!fieldValid) {
                    $(`#err_${field.id}`).show();
                } else {
                    $(`#err_${field.id}`).hide();
                }
                break;
        }
        
        if (!fieldValid) {
            isValid = false;
        }
    });
    
    return isValid;
}

/**
 * Submit the form and save data
 */
function submitForm(formId) {
    const formData = {};
    
    formConfig.fields.forEach(field => {
        let value;
        
        switch(field.type) {
            case 'text':
            case 'number':
            case 'email':
            case 'date':
            case 'select':
                value = $(`#${field.id}`).val();
                formData[field.id] = value;
                break;
                
            case 'radio':
                value = $(`input[name='${field.id}']:checked`).val();
                formData[field.id] = value || '';
                break;
                
            case 'checkbox':
                const checked = $(`input[name='${field.id}[]']:checked`);
                const values = [];
                
                checked.each(function() {
                    values.push($(this).val());
                });
                
                formData[field.id] = values;
                break;
        }
    });
    
    // Add timestamp
    formData.timestamp = new Date().toLocaleString();
    
    // Get existing data
    let existingData = [];
    try {
        const dataString = localStorage.getItem(formDataKey + formId);
        if (dataString) {
            existingData = JSON.parse(dataString);
        }
    } catch (e) {
        console.error('Error loading existing data:', e);
    }
    
    // Add new data
    existingData.push(formData);
    
    // Save data
    localStorage.setItem(formDataKey + formId, JSON.stringify(existingData));
    
    // Reload data
    loadSubmittedData(formId);
    
    // Reset form
    $('#dynamicForm')[0].reset();
    
    // Show success message
    alert('Form submitted successfully!');
}

/**
 * Load submitted data from localStorage
 */
function loadSubmittedData(formId) {
    try {
        const dataString = localStorage.getItem(formDataKey + formId);
        
        if (!dataString) {
            // No data yet
            $('#dataTable tbody').html('<tr><td colspan="' + (formConfig.fields.length + 2) + '" class="text-center">No data submitted yet</td></tr>');
            return;
        }
        
        submittedData = JSON.parse(dataString);
        
        // Clear existing rows
        $('#dataTable tbody').empty();
        
        // Add data rows
        submittedData.forEach((data, index) => {
            let rowHtml = `<tr><td>${index + 1}</td>`;
            
            formConfig.fields.forEach(field => {
                let cellValue = '';
                
                if (field.type === 'checkbox') {
                    cellValue = Array.isArray(data[field.id]) ? data[field.id].join(', ') : data[field.id] || '';
                } else {
                    cellValue = data[field.id] || '';
                }
                
                rowHtml += `<td>${cellValue}</td>`;
            });
            
            // Add timestamp
            rowHtml += `<td>${data.timestamp || ''}</td></tr>`;
            
            $('#dataTable tbody').append(rowHtml);
        });
        
    } catch (e) {
        console.error('Error loading submitted data:', e);
        $('#dataTable tbody').html('<tr><td colspan="' + (formConfig.fields.length + 2) + '" class="text-center">Error loading data</td></tr>');
    }
}
