/**
 * Property panel management for components
 */

/**
 * Show properties for the selected component
 */
function showComponentProperties(component, componentType) {
    let propertiesHtml = '';
    
    // Generate properties panel content based on component type
    switch(componentType) {
        case 'banner':
            propertiesHtml = getBannerProperties(component);
            break;
        case 'navbar':
            propertiesHtml = getNavbarProperties(component);
            break;
        case 'table':
            propertiesHtml = getTableProperties(component);
            break;
        case 'text-field':
            propertiesHtml = getTextFieldProperties(component);
            break;
        case 'email-field':
            propertiesHtml = getEmailFieldProperties(component);
            break;
        case 'date-field':
            propertiesHtml = getDateFieldProperties(component);
            break;
        case 'select':
            propertiesHtml = getSelectProperties(component);
            break;
        case 'radio-group':
            propertiesHtml = getRadioGroupProperties(component);
            break;
        case 'checkbox-group':
            propertiesHtml = getCheckboxGroupProperties(component);
            break;
        case 'modal':
            propertiesHtml = getModalProperties(component);
            break;
        case 'button':
            propertiesHtml = getButtonProperties(component);
            break;
        case 'footer':
            propertiesHtml = getFooterProperties(component);
            break;
        default:
            propertiesHtml = '<p class="text-center text-muted">No properties available</p>';
    }
    
    // Update properties panel
    $('#properties-panel').html(propertiesHtml);
    
    // Initialize property change handlers
    initPropertyHandlers(component, componentType);
}

/**
 * Get properties for banner component
 */
function getBannerProperties(component) {
    const imgSrc = component.find('img').attr('src') || 'https://via.placeholder.com/800x200?text=Banner+Image';
    const imgAlt = component.find('img').attr('alt') || 'Banner';
    
    return `
        <div class="property-group">
            <label for="banner-image-url">Đường dẫn hình ảnh:</label>
            <input type="text" class="form-control form-control-sm" id="banner-image-url" value="${imgSrc}">
        </div>
        <div class="property-group">
            <label for="banner-alt-text">Mô tả ảnh:</label>
            <input type="text" class="form-control form-control-sm" id="banner-alt-text" value="${imgAlt}">
        </div>
        <div class="property-group">
            <label for="banner-height">Chiều cao (px):</label>
            <input type="number" class="form-control form-control-sm" id="banner-height" value="200" min="50" max="500">
        </div>
    `;
}

/**
 * Get properties for navbar component
 */
function getNavbarProperties(component) {
    const navItems = [];
    component.find('.navbar-nav li:not(:first-child):not(:last-child) a').each(function() {
        navItems.push($(this).text());
    });
    
    const brandName = component.find('.navbar-nav li:first-child a').text();
    const bgClass = component.find('nav').attr('class').match(/bg-\w+/) ? 
                   component.find('nav').attr('class').match(/bg-\w+/)[0].replace('bg-', '') : 'light';
    
    return `
        <div class="property-group">
            <label for="navbar-brand">Tên thương hiệu:</label>
            <input type="text" class="form-control form-control-sm" id="navbar-brand" value="${brandName}">
        </div>
        <div class="property-group">
            <label for="navbar-bg">Màu nền:</label>
            <select class="form-control form-control-sm" id="navbar-bg">
                <option value="light" ${bgClass === 'light' ? 'selected' : ''}>Sáng</option>
                <option value="dark" ${bgClass === 'dark' ? 'selected' : ''}>Tối</option>
                <option value="primary" ${bgClass === 'primary' ? 'selected' : ''}>Chính</option>
                <option value="secondary" ${bgClass === 'secondary' ? 'selected' : ''}>Phụ</option>
            </select>
        </div>
        <div class="property-group">
            <label for="navbar-items">Các mục điều hướng:</label>
            <textarea class="form-control form-control-sm" id="navbar-items" rows="4">${navItems.join('\n')}</textarea>
            <small class="form-text text-muted">Mỗi mục trên một dòng</small>
        </div>
        <div class="property-group">
            <label for="navbar-register-text">Nút đăng ký:</label>
            <input type="text" class="form-control form-control-sm" id="navbar-register-text" value="${component.find('.navbar-nav li:last-child a').text()}">
        </div>
    `;
}

/**
 * Get properties for table component
 */
function getTableProperties(component) {
    const title = component.find('h3').text();
    const headers = [];
    component.find('thead th').each(function() {
        headers.push($(this).text());
    });
    
    const tableClass = component.find('table').attr('class');
    const isBordered = tableClass.includes('table-bordered');
    const isStriped = tableClass.includes('table-striped');
    
    return `
        <div class="property-group">
            <label for="table-title">Tiêu đề bảng:</label>
            <input type="text" class="form-control form-control-sm" id="table-title" value="${title}">
        </div>
        <div class="property-group">
            <label for="table-headers">Các cột:</label>
            <textarea class="form-control form-control-sm" id="table-headers" rows="4">${headers.join('\n')}</textarea>
            <small class="form-text text-muted">Mỗi cột trên một dòng</small>
        </div>
        <div class="property-group">
            <div class="custom-control custom-checkbox">
                <input type="checkbox" class="custom-control-input" id="table-bordered" ${isBordered ? 'checked' : ''}>
                <label class="custom-control-label" for="table-bordered">Bảng có viền</label>
            </div>
        </div>
        <div class="property-group">
            <div class="custom-control custom-checkbox">
                <input type="checkbox" class="custom-control-input" id="table-striped" ${isStriped ? 'checked' : ''}>
                <label class="custom-control-label" for="table-striped">Hàng sọc</label>
            </div>
        </div>
    `;
}

/**
 * Get properties for text field component
 */
function getTextFieldProperties(component) {
    const label = component.find('label').text();
    const inputId = component.find('input').attr('id');
    const placeholder = component.find('input').attr('placeholder') || '';
    const required = component.find('input').prop('required') || false;
    
    return `
        <div class="property-group">
            <label for="text-field-label">Nhãn trường:</label>
            <input type="text" class="form-control form-control-sm" id="text-field-label" value="${label}">
        </div>
        <div class="property-group">
            <label for="text-field-id">ID trường:</label>
            <input type="text" class="form-control form-control-sm" id="text-field-id" value="${inputId}">
            <small class="form-text text-muted">Dùng cho việc gửi biểu mẫu</small>
        </div>
        <div class="property-group">
            <label for="text-field-placeholder">Gợi ý:</label>
            <input type="text" class="form-control form-control-sm" id="text-field-placeholder" value="${placeholder}">
        </div>
        <div class="property-group">
            <div class="custom-control custom-checkbox">
                <input type="checkbox" class="custom-control-input" id="text-field-required" ${required ? 'checked' : ''}>
                <label class="custom-control-label" for="text-field-required">Bắt buộc</label>
            </div>
        </div>
        <div class="property-group">
            <label for="text-field-validation">Kiểu xác thực:</label>
            <select class="form-control form-control-sm" id="text-field-validation">
                <option value="none">Không có</option>
                <option value="name">Tên (Chữ đầu viết hoa)</option>
                <option value="phone">Số điện thoại</option>
            </select>
        </div>
    `;
}

/**
 * Get properties for email field component
 */
function getEmailFieldProperties(component) {
    const label = component.find('label').text();
    const inputId = component.find('input').attr('id');
    const placeholder = component.find('input').attr('placeholder') || '';
    const required = component.find('input').prop('required') || false;
    
    return `
        <div class="property-group">
            <label for="email-field-label">Nhãn Email:</label>
            <input type="text" class="form-control form-control-sm" id="email-field-label" value="${label}">
        </div>
        <div class="property-group">
            <label for="email-field-id">ID trường:</label>
            <input type="text" class="form-control form-control-sm" id="email-field-id" value="${inputId}">
        </div>
        <div class="property-group">
            <label for="email-field-placeholder">Gợi ý:</label>
            <input type="text" class="form-control form-control-sm" id="email-field-placeholder" value="${placeholder}">
        </div>
        <div class="property-group">
            <div class="custom-control custom-checkbox">
                <input type="checkbox" class="custom-control-input" id="email-field-required" ${required ? 'checked' : ''}>
                <label class="custom-control-label" for="email-field-required">Bắt buộc</label>
            </div>
        </div>
    `;
}

/**
 * Get properties for date field component
 */
function getDateFieldProperties(component) {
    const label = component.find('label').text();
    const inputId = component.find('input').attr('id');
    const required = component.find('input').prop('required') || false;
    
    return `
        <div class="property-group">
            <label for="date-field-label">Nhãn ngày:</label>
            <input type="text" class="form-control form-control-sm" id="date-field-label" value="${label}">
        </div>
        <div class="property-group">
            <label for="date-field-id">ID trường:</label>
            <input type="text" class="form-control form-control-sm" id="date-field-id" value="${inputId}">
        </div>
        <div class="property-group">
            <div class="custom-control custom-checkbox">
                <input type="checkbox" class="custom-control-input" id="date-field-required" ${required ? 'checked' : ''}>
                <label class="custom-control-label" for="date-field-required">Bắt buộc</label>
            </div>
        </div>
        <div class="property-group">
            <div class="custom-control custom-checkbox">
                <input type="checkbox" class="custom-control-input" id="date-field-past-only" checked>
                <label class="custom-control-label" for="date-field-past-only">Phải là ngày trong quá khứ</label>
            </div>
        </div>
    `;
}

/**
 * Get properties for select dropdown component
 */
function getSelectProperties(component) {
    const label = component.find('label').text();
    const selectId = component.find('select').attr('id');
    
    // Extract options
    const options = [];
    component.find('select option').each(function() {
        options.push($(this).text());
    });
    
    return `
        <div class="property-group">
            <label for="select-field-label">Nhãn dropdown:</label>
            <input type="text" class="form-control form-control-sm" id="select-field-label" value="${label}">
        </div>
        <div class="property-group">
            <label for="select-field-id">ID trường:</label>
            <input type="text" class="form-control form-control-sm" id="select-field-id" value="${selectId}">
        </div>
        <div class="property-group">
            <label for="select-options">Các lựa chọn:</label>
            <textarea class="form-control form-control-sm" id="select-options" rows="4">${options.join('\n')}</textarea>
            <small class="form-text text-muted">Mỗi lựa chọn trên một dòng</small>
        </div>
        <div class="property-group">
            <div class="custom-control custom-checkbox">
                <input type="checkbox" class="custom-control-input" id="select-has-duration" checked>
                <label class="custom-control-label" for="select-has-duration">Có giá trị thời gian học</label>
            </div>
        </div>
    `;
}

/**
 * Get properties for radio group component
 */
function getRadioGroupProperties(component) {
    const label = component.find('label:first').text();
    const groupName = component.find('input[type="radio"]').attr('name');
    
    // Extract options
    const options = [];
    component.find('.form-check').each(function() {
        options.push($(this).find('label').text());
    });
    
    return `
        <div class="property-group">
            <label for="radio-group-label">Nhãn nhóm:</label>
            <input type="text" class="form-control form-control-sm" id="radio-group-label" value="${label}">
        </div>
        <div class="property-group">
            <label for="radio-group-name">Tên nhóm:</label>
            <input type="text" class="form-control form-control-sm" id="radio-group-name" value="${groupName}">
        </div>
        <div class="property-group">
            <label for="radio-options">Các lựa chọn:</label>
            <textarea class="form-control form-control-sm" id="radio-options" rows="4">${options.join('\n')}</textarea>
            <small class="form-text text-muted">Mỗi lựa chọn trên một dòng</small>
        </div>
    `;
}

/**
 * Get properties for checkbox group component
 */
function getCheckboxGroupProperties(component) {
    const label = component.find('label:first').text();
    
    // Extract options
    const options = [];
    component.find('.form-check').each(function() {
        options.push($(this).find('label').text());
    });
    
    return `
        <div class="property-group">
            <label for="checkbox-group-label">Nhãn nhóm:</label>
            <input type="text" class="form-control form-control-sm" id="checkbox-group-label" value="${label}">
        </div>
        <div class="property-group">
            <label for="checkbox-options">Các lựa chọn:</label>
            <textarea class="form-control form-control-sm" id="checkbox-options" rows="4">${options.join('\n')}</textarea>
            <small class="form-text text-muted">Mỗi lựa chọn trên một dòng</small>
        </div>
        <div class="property-group">
            <div class="custom-control custom-checkbox">
                <input type="checkbox" class="custom-control-input" id="checkbox-required" checked>
                <label class="custom-control-label" for="checkbox-required">Yêu cầu chọn ít nhất một mục</label>
            </div>
        </div>
    `;
}

/**
 * Get properties for modal component
 */
function getModalProperties(component) {
    return `
        <div class="property-group">
            <label for="modal-title">Tiêu đề modal:</label>
            <input type="text" class="form-control form-control-sm" id="modal-title" value="THÔNG TIN ĐĂNG KÍ">
        </div>
        <div class="property-group">
            <label for="modal-id">ID modal:</label>
            <input type="text" class="form-control form-control-sm" id="modal-id" value="myModal">
        </div>
        <div class="property-group">
            <label for="modal-submit">Nút gửi:</label>
            <input type="text" class="form-control form-control-sm" id="modal-submit" value="Đăng kí">
        </div>
        <div class="property-group">
            <label for="modal-cancel">Nút hủy:</label>
            <input type="text" class="form-control form-control-sm" id="modal-cancel" value="Hủy">
        </div>
        <div class="property-group">
            <p class="mb-1">Kích thước modal:</p>
            <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="modal-size" id="modal-size-sm" value="modal-sm">
                <label class="form-check-label" for="modal-size-sm">Nhỏ</label>
            </div>
            <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="modal-size" id="modal-size-default" value="">
                <label class="form-check-label" for="modal-size-default">Mặc định</label>
            </div>
            <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="modal-size" id="modal-size-lg" value="modal-lg" checked>
                <label class="form-check-label" for="modal-size-lg">Lớn</label>
            </div>
        </div>
    `;
}

/**
 * Get properties for button component
 */
function getButtonProperties(component) {
    const buttonText = component.find('button').text();
    const buttonClass = component.find('button').attr('class');
    const variant = buttonClass.match(/btn-\w+/) ? buttonClass.match(/btn-\w+/)[0].replace('btn-', '') : 'primary';
    
    return `
        <div class="property-group">
            <label for="button-text">Nội dung nút:</label>
            <input type="text" class="form-control form-control-sm" id="button-text" value="${buttonText}">
        </div>
        <div class="property-group">
            <label for="button-variant">Kiểu nút:</label>
            <select class="form-control form-control-sm" id="button-variant">
                <option value="primary" ${variant === 'primary' ? 'selected' : ''}>Primary</option>
                <option value="secondary" ${variant === 'secondary' ? 'selected' : ''}>Secondary</option>
                <option value="success" ${variant === 'success' ? 'selected' : ''}>Success</option>
                <option value="danger" ${variant === 'danger' ? 'selected' : ''}>Danger</option>
                <option value="warning" ${variant === 'warning' ? 'selected' : ''}>Warning</option>
                <option value="info" ${variant === 'info' ? 'selected' : ''}>Info</option>
                <option value="light" ${variant === 'light' ? 'selected' : ''}>Light</option>
                <option value="dark" ${variant === 'dark' ? 'selected' : ''}>Dark</option>
            </select>
        </div>
        <div class="property-group">
            <label for="button-action">Hành động:</label>
            <select class="form-control form-control-sm" id="button-action">
                <option value="none">Không hành động</option>
                <option value="submit">Gửi form</option>
                <option value="modal">Mở modal</option>
                <option value="custom">Hàm tùy chỉnh</option>
            </select>
        </div>
    `;
}

/**
 * Get properties for footer component
 */
function getFooterProperties(component) {
    const bgColor = component.find('#footer').css('background-color') || '#007bff';
    const studentName = component.find('p:contains("Họ tên")').text().replace('Họ tên: ', '');
    const studentId = component.find('p:contains("Mã sinh viên")').text().replace('Mã sinh viên: ', '');
    const classId = component.find('p:contains("Mã lớp")').text().replace('Mã lớp: ', '');
    
    return `
        <div class="property-group">
            <label for="footer-bg-color">Màu nền:</label>
            <input type="color" class="form-control form-control-sm" id="footer-bg-color" value="#007bff">
            <small class="form-text text-muted">Chọn màu nền cho footer</small>
        </div>
        <div class="property-group">
            <label for="footer-title">Tiêu đề:</label>
            <input type="text" class="form-control form-control-sm" id="footer-title" value="Thông tin sinh viên">
        </div>
        <div class="property-group">
            <label for="footer-student-name">Họ tên:</label>
            <input type="text" class="form-control form-control-sm" id="footer-student-name" value="${studentName}">
        </div>
        <div class="property-group">
            <label for="footer-student-id">Mã sinh viên:</label>
            <input type="text" class="form-control form-control-sm" id="footer-student-id" value="${studentId}">
        </div>
        <div class="property-group">
            <label for="footer-class-id">Mã lớp:</label>
            <input type="text" class="form-control form-control-sm" id="footer-class-id" value="${classId}">
        </div>
    `;
}

/**
 * Initialize property change handlers
 */
function initPropertyHandlers(component, componentType) {
    // Set up handlers based on component type
    switch(componentType) {
        case 'banner':
            initBannerHandlers(component);
            break;
        case 'navbar':
            initNavbarHandlers(component);
            break;
        case 'table':
            initTableHandlers(component);
            break;
        case 'text-field':
            initTextFieldHandlers(component);
            break;
        case 'email-field':
            initEmailFieldHandlers(component);
            break;
        case 'date-field':
            initDateFieldHandlers(component);
            break;
        case 'select':
            initSelectHandlers(component);
            break;
        case 'radio-group':
            initRadioGroupHandlers(component);
            break;
        case 'checkbox-group':
            initCheckboxGroupHandlers(component);
            break;
        case 'modal':
            initModalHandlers(component);
            break;
        case 'button':
            initButtonHandlers(component);
            break;
        case 'footer':
            initFooterHandlers(component);
            break;
    }
}

/**
 * Banner property handlers
 */
function initBannerHandlers(component) {
    $('#banner-image-url').on('change', function() {
        component.find('img').attr('src', $(this).val());
    });
    
    $('#banner-alt-text').on('change', function() {
        component.find('img').attr('alt', $(this).val());
    });
    
    $('#banner-height').on('input change', function() {
        component.find('img').css('height', $(this).val() + 'px');
    });
}

/**
 * Navbar property handlers
 */
function initNavbarHandlers(component) {
    $('#navbar-brand').on('change', function() {
        component.find('.navbar-nav li:first-child a').text($(this).val());
    });
    
    $('#navbar-bg').on('change', function() {
        const nav = component.find('nav');
        nav.removeClass('bg-light bg-dark bg-primary bg-secondary')
           .addClass('bg-' + $(this).val());
           
        // Adjust text color for dark background
        if ($(this).val() === 'dark') {
            nav.addClass('navbar-dark');
        } else {
            nav.removeClass('navbar-dark');
        }
    });
    
    $('#navbar-items').on('change', function() {
        const items = $(this).val().split('\n');
        const navUl = component.find('.navbar-nav');
        
        // Keep first and last items (brand and register button)
        const firstItem = navUl.find('li:first-child').clone();
        const lastItem = navUl.find('li:last-child').clone();
        
        // Clear nav items
        navUl.empty();
        navUl.append(firstItem);
        
        // Add new items
        items.forEach(item => {
            if (item.trim()) {
                navUl.append(`
                    <li class="nav-item">
                        <a class="nav-link" href="#">${item}</a>
                    </li>
                `);
            }
        });
        
        navUl.append(lastItem);
    });
    
    $('#navbar-register-text').on('change', function() {
        component.find('.navbar-nav li:last-child a').text($(this).val());
    });
}

/**
 * Table property handlers
 */
function initTableHandlers(component) {
    $('#table-title').on('change', function() {
        component.find('h3').text($(this).val());
    });
    
    $('#table-headers').on('change', function() {
        const headers = $(this).val().split('\n');
        const headerRow = component.find('thead tr');
        headerRow.empty();
        
        headers.forEach(header => {
            if (header.trim()) {
                headerRow.append(`<th>${header}</th>`);
            }
        });
    });
    
    $('#table-bordered').on('change', function() {
        if ($(this).is(':checked')) {
            component.find('table').addClass('table-bordered');
        } else {
            component.find('table').removeClass('table-bordered');
        }
    });
    
    $('#table-striped').on('change', function() {
        if ($(this).is(':checked')) {
            component.find('table').addClass('table-striped');
        } else {
            component.find('table').removeClass('table-striped');
        }
    });
}

/**
 * Text field property handlers
 */
function initTextFieldHandlers(component) {
    $('#text-field-label').on('change', function() {
        component.find('label').text($(this).val());
    });
    
    $('#text-field-id').on('change', function() {
        const oldId = component.find('input').attr('id');
        const newId = $(this).val();
        
        component.find('input').attr('id', newId);
        component.find('label').attr('for', newId);
        component.find('span.text-danger').attr('id', 'er' + newId.substring(3));
    });
    
    $('#text-field-placeholder').on('change', function() {
        component.find('input').attr('placeholder', $(this).val());
    });
    
    $('#text-field-required').on('change', function() {
        if ($(this).is(':checked')) {
            component.find('input').attr('required', 'required');
        } else {
            component.find('input').removeAttr('required');
        }
    });
}

/**
 * Email field property handlers
 */
function initEmailFieldHandlers(component) {
    $('#email-field-label').on('change', function() {
        component.find('label').text($(this).val());
    });
    
    $('#email-field-id').on('change', function() {
        const oldId = component.find('input').attr('id');
        const newId = $(this).val();
        
        component.find('input').attr('id', newId);
        component.find('label').attr('for', newId);
        component.find('span.text-danger').attr('id', 'er' + newId.substring(3));
    });
    
    $('#email-field-placeholder').on('change', function() {
        component.find('input').attr('placeholder', $(this).val());
    });
    
    $('#email-field-required').on('change', function() {
        if ($(this).is(':checked')) {
            component.find('input').attr('required', 'required');
        } else {
            component.find('input').removeAttr('required');
        }
    });
}

/**
 * Date field property handlers
 */
function initDateFieldHandlers(component) {
    $('#date-field-label').on('change', function() {
        component.find('label').text($(this).val());
    });
    
    $('#date-field-id').on('change', function() {
        const oldId = component.find('input').attr('id');
        const newId = $(this).val();
        
        component.find('input').attr('id', newId);
        component.find('label').attr('for', newId);
        component.find('span.text-danger').attr('id', 'er' + newId.substring(3));
    });
    
    $('#date-field-required').on('change', function() {
        if ($(this).is(':checked')) {
            component.find('input').attr('required', 'required');
        } else {
            component.find('input').removeAttr('required');
        }
    });
}

/**
 * Select dropdown property handlers
 */
function initSelectHandlers(component) {
    $('#select-field-label').on('change', function() {
        component.find('label').text($(this).val());
    });
    
    $('#select-field-id').on('change', function() {
        const newId = $(this).val();
        component.find('select').attr('id', newId);
        component.find('label').attr('for', newId);
    });
    
    $('#select-options').on('change', function() {
        const options = $(this).val().split('\n');
        const select = component.find('select');
        select.empty();
        
        options.forEach((option, index) => {
            if (option.trim()) {
                // If it's a course with duration, use duration as value
                const value = $('#select-has-duration').is(':checked') ? (index + 1) * 3 : option.toLowerCase().replace(/\s+/g, '-');
                select.append(`<option value="${value}" data-name="${option.trim()}">${option.trim()}</option>`);
            }
        });
    });
}

/**
 * Radio group property handlers
 */
function initRadioGroupHandlers(component) {
    $('#radio-group-label').on('change', function() {
        component.find('label:first').text($(this).val());
    });
    
    $('#radio-group-name').on('change', function() {
        const newName = $(this).val();
        component.find('input[type="radio"]').attr('name', newName);
    });
    
    $('#radio-options').on('change', function() {
        const options = $(this).val().split('\n');
        const container = component.find('.col-9');
        const name = component.find('input[type="radio"]').attr('name');
        container.empty();
        
        options.forEach((option, index) => {
            if (option.trim()) {
                const id = `radio${index + 1}${component.attr('id')}`;
                const checked = index === 0 ? 'checked' : '';
                container.append(`
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="${name}" id="${id}" value="${option.trim()}" ${checked}>
                        <label class="form-check-label" for="${id}">${option.trim()}</label>
                    </div>
                `);
            }
        });
        
        container.append(`<span id="erRadio${component.attr('id')}" class="text-danger small mt-1 d-block"></span>`);
    });
}

/**
 * Checkbox group property handlers
 */
function initCheckboxGroupHandlers(component) {
    $('#checkbox-group-label').on('change', function() {
        component.find('label:first').text($(this).val());
    });
    
    $('#checkbox-options').on('change', function() {
        const options = $(this).val().split('\n');
        const container = component.find('.col-9');
        container.empty();
        
        options.forEach((option, index) => {
            if (option.trim()) {
                const id = `chk${index + 1}${component.attr('id')}`;
                container.append(`
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="${id}" value="${option.trim()}">
                        <label class="form-check-label" for="${id}">${option.trim()}</label>
                    </div>
                `);
            }
        });
        
        container.append(`<span id="erCheck${component.attr('id')}" class="text-danger small mt-1 d-block"></span>`);
    });
}

/**
 * Modal property handlers
 */
function initModalHandlers(component) {
    // Modal properties are mainly used at code generation time
    // Since the modal preview is just a placeholder
}

/**
 * Button property handlers
 */
function initButtonHandlers(component) {
    $('#button-text').on('change', function() {
        component.find('button').text($(this).val());
    });
    
    $('#button-variant').on('change', function() {
        const btn = component.find('button');
        btn.removeClass(function(index, className) {
            return (className.match(/(^|\s)btn-\S+/g) || []).join(' ');
        });
        btn.addClass(`btn-${$(this).val()}`);
    });
}

/**
 * Footer property handlers
 */
function initFooterHandlers(component) {
    $('#footer-bg-color').on('change', function() {
        component.find('#footer').css('background-color', $(this).val());
    });
    
    $('#footer-title').on('change', function() {
        component.find('h5').text($(this).val());
    });
    
    $('#footer-student-name').on('change', function() {
        component.find('p:contains("Họ tên")').text('Họ tên: ' + $(this).val());
    });
    
    $('#footer-student-id').on('change', function() {
        component.find('p:contains("Mã sinh viên")').text('Mã sinh viên: ' + $(this).val());
    });
    
    $('#footer-class-id').on('change', function() {
        component.find('p:contains("Mã lớp")').text('Mã lớp: ' + $(this).val());
    });
}
