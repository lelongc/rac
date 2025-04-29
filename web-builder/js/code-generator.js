/**
 * Code generation for exporting the created page
 */

/**
 * Generate HTML code from the canvas
 * @param {boolean} isPreview - Whether generating for preview (includes validation scripts)
 */
function generateHTMLCode(isPreview = false) {
    const pageTitle = $('#page-title').val();
    const language = $('#page-language').val();
    const hasModal = $('#canvas .canvas-component[data-type="modal"]').length > 0;
    
    // Clone canvas content for modification
    const canvasContent = $('#canvas').clone();
    
    // Remove all component controls and classes
    canvasContent.find('.component-actions').remove();
    canvasContent.find('.canvas-component').removeClass('canvas-component selected');
    canvasContent.find('.drop-placeholder').remove();
    
    // Begin HTML document
    let html = `<!DOCTYPE html>
<html lang="${language}">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${pageTitle}</title>
    <link rel="stylesheet" href="${isPreview ? 'https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css' : '../css/bootstrap.min.css'}">
    <style>
        * {
            box-sizing: border-box;
            padding: 0;
            margin: 0;
            color: black;
        }

        body {
            font-size: 16px;
            line-height: 1.5;
        }

        #header {
            overflow: hidden;
        }
    </style>
</head>

<body>
    <!-- Main container -->
    <div class="container" style="border: 1px solid black;">`;
    
    // Add contents from canvas
    html += canvasContent.html();
    
    // If there's a modal component referenced but not in the canvas,
    // generate the modal code
    if (hasModal) {
        html += generateModalHTML();
    }
    
    // Close main container
    html += `
    </div>

    <!-- JavaScript libraries -->
    <script src="${isPreview ? 'https://code.jquery.com/jquery-3.7.1.min.js' : '../js/jquery-3.7.1.min.js'}"></script>
    <script src="${isPreview ? 'https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.min.js' : '../js/bootstrap.min.js'}"></script>
    <script src="${isPreview ? 'javascript:' + encodeURIComponent(generateJSCode()) : '../js/main.js'}"></script>
</body>

</html>`;

    return html;
}

/**
 * Generate a modal HTML based on modal settings
 */
function generateModalHTML() {
    const modalId = $('#modal-id').val() || 'myModal';
    const modalTitle = $('#modal-title').val() || 'THÔNG TIN ĐĂNG KÍ';
    const modalSubmit = $('#modal-submit').val() || 'Đăng kí';
    const modalCancel = $('#modal-cancel').val() || 'Hủy';
    const modalSize = $('input[name="modal-size"]:checked').val() || 'modal-lg';
    
    return `
        <!-- Registration modal -->
        <div class="modal fade" id="${modalId}">
            <div class="modal-dialog ${modalSize}">
                <div class="modal-content">
                    <!-- Modal header -->
                    <div class="modal-header">
                        <h2>${modalTitle}</h2>
                        <button type="button" class="close" data-dismiss="modal">&times;</button>
                    </div>

                    <!-- Modal body with registration form -->
                    <div class="modal-body">
                        <div class="form-group">
                            <!-- Full name -->
                            <div class="row mt-2">
                                <div class="col-3 text-right">
                                    <label for="txtName" class="font-weight-normal">Họ và tên</label>
                                </div>
                                <div class="col-9">
                                    <input type="text" id="txtName" class="form-control">
                                    <span id="erName" class="text-danger small mt-1 d-block"></span>
                                </div>
                            </div>

                            <!-- Phone number -->
                            <div class="row mt-2">
                                <div class="col-3 text-right">
                                    <label for="txtSDT" class="font-weight-normal">Số điện thoại</label>
                                </div>
                                <div class="col-9">
                                    <input type="text" id="txtSDT" class="form-control">
                                    <span id="erSDT" class="text-danger small mt-1 d-block"></span>
                                </div>
                            </div>

                            <!-- Date of birth -->
                            <div class="row mt-2">
                                <div class="col-3 text-right">
                                    <label for="txtNgaysinh" class="font-weight-normal">Ngày sinh</label>
                                </div>
                                <div class="col-9">
                                    <input type="date" id="txtNgaysinh" class="form-control">
                                    <span id="erNgaysinh" class="text-danger small mt-1 d-block"></span>
                                </div>
                            </div>

                            <!-- Email -->
                            <div class="row mt-2">
                                <div class="col-3 text-right">
                                    <label for="txtEmail" class="font-weight-normal">Email</label>
                                </div>
                                <div class="col-9">
                                    <input type="email" id="txtEmail" class="form-control" placeholder="your.email@example.com">
                                    <span id="erEmail" class="text-danger small mt-1 d-block"></span>
                                </div>
                            </div>

                            <!-- Course selection -->
                            <div class="row mt-2">
                                <div class="col-3 text-right">
                                    <label for="slKhoahoc" class="font-weight-normal">Khóa học</label>
                                </div>
                                <div class="col-9">
                                    <select id="slKhoahoc" class="form-control">
                                        <option value="3" data-name="Anh văn cơ bản">Anh văn cơ bản</option>
                                        <option value="6" data-name="Anh văn giao tiếp">Anh văn giao tiếp</option>
                                        <option value="12" data-name="Luyện thi IELTS">Luyện thi IELTS</option>
                                    </select>
                                </div>
                            </div>

                            <!-- Study duration -->
                            <div class="row mt-2">
                                <div class="col-3 text-right">
                                    <label for="txtThoiGianHoc" class="font-weight-normal">Thời gian học</label>
                                </div>
                                <div class="col-9">
                                    <input type="text" id="txtThoiGianHoc" class="form-control" readonly>
                                </div>
                            </div>

                            <!-- Study method -->
                            <div class="row mt-2">
                                <div class="col-3 text-right">
                                    <label for="radioHinhthuc" class="font-weight-normal">Hình thức học</label>
                                </div>
                                <div class="col-9">
                                    <div class="form-check">
                                        <input class="form-check-input" type="radio" name="hinhthuc" id="radioCenter" value="Học tại trung tâm" checked>
                                        <label class="form-check-label" for="radioCenter">Học tại trung tâm</label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="radio" name="hinhthuc" id="radioOnline" value="Học online">
                                        <label class="form-check-label" for="radioOnline">Học online</label>
                                    </div>
                                    <span id="erHinhthuc" class="text-danger small mt-1 d-block"></span>
                                </div>
                            </div>

                            <!-- Skills needed -->
                            <div class="row mt-2">
                                <div class="col-3 text-right">
                                    <label for="chkSkills" class="font-weight-normal">Kỹ năng cần luyện</label>
                                </div>
                                <div class="col-9">
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" id="chkListening" value="Kỹ năng nghe">
                                        <label class="form-check-label" for="chkListening">Kỹ năng nghe</label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" id="chkReading" value="Kỹ năng đọc">
                                        <label class="form-check-label" for="chkReading">Kỹ năng đọc</label>
                                    </div>
                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" id="chkWriting" value="Kỹ năng viết">
                                        <label class="form-check-label" for="chkWriting">Kỹ năng viết</label>
                                    </div>
                                    <span id="erSkills" class="text-danger small mt-1 d-block"></span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Modal footer -->
                    <div class="modal-footer d-flex justify-content-end">
                        <button type="button" class="btn btn-success btn-sm mr-2" onclick="DangKy()">${modalSubmit}</button>
                        <button type="button" class="btn btn-danger btn-sm" data-dismiss="modal">${modalCancel}</button>
                    </div>
                </div>
            </div>
        </div>
    `;
}

/**
 * Generate JavaScript code for the page
 */
function generateJSCode() {
    return `/**
 * Validate the name field
 * Requirements: Not empty, each word must start with uppercase (e.g., Le Van An)
 */
function checkName() {
    var name = $("#txtName").val();
    
    // Check if name is empty
    if (name.trim() === "") {
        $("#erName").text("Họ tên không được để trống");
        return false;
    }
    
    // Use regex to validate name format: words starting with uppercase, followed by lowercase
    // Must have at least two words separated by spaces
    var regex = /^[A-Z][a-z]*(\s+[A-Z][a-z]*)+$/;
    if (!regex.test(name)) {
        $("#erName").text("Mỗi từ phải bắt đầu bằng chữ hoa và phần còn lại viết thường");
        return false;
    }
    
    $("#erName").text("");
    return true;
}

/**
 * Validate the date of birth field
 * Requirements: Not empty, must be before current date
 */
function checkDateOfBirth() {
    var dob = $("#txtNgaysinh").val();
    var today = new Date();
    var dobDate = new Date(dob);

    if (dob === "") {
        $("#erNgaysinh").text("Ngày sinh không được rỗng");
        return false;
    } else if (dobDate >= today) {
        $("#erNgaysinh").text("Ngày sinh phải trước ngày hiện tại");
        return false;
    } else {
        $("#erNgaysinh").text("");
        return true;
    }
}

/**
 * Validate the phone number field
 * Requirements: Not empty, 10 digits starting with 09, 03, or 08
 */
function checkPhoneNum() {
    var phone = $("#txtSDT").val();
    
    // Check if phone is empty
    if (phone.trim() === "") {
        $("#erSDT").text("Số điện thoại không được để trống");
        return false;
    }
    
    // Check phone format: 10 digits starting with 09, 03, or 08
    var regex = /^(09|03|08)\\d{8}$/;
    if (!regex.test(phone)) {
        $("#erSDT").text("Số điện thoại phải có 10 số và bắt đầu với 09, 03 hoặc 08");
        return false;
    }
    
    $("#erSDT").text("");
    return true;
}

/**
 * Validate the email field
 * Requirements: Must contain @ and end with .com
 */
function checkEmail() {
    var email = $("#txtEmail").val();
    
    // Check email format: must contain @ and end with .com
    var regex = /@.*\\.com$/;
    if (!regex.test(email)) {
        $("#erEmail").text("Email phải chứa @ và kết thúc với .com");
        return false;
    }
    
    $("#erEmail").text("");
    return true;
}

/**
 * Validate the study method selection
 * Requirements: At least one option must be selected
 */
function checkStudyMethod() {
    // Check if a study method is selected
    if (!$("input[name='hinhthuc']:checked").length) {
        $("#erHinhthuc").text("Vui lòng chọn hình thức học");
        return false;
    }
    $("#erHinhthuc").text("");
    return true;
}

/**
 * Validate the skills selection
 * Requirements: At least one skill must be selected
 */
function checkSkills() {
    // Check if at least one skill is selected
    if (!$("#chkListening").is(":checked") && 
        !$("#chkReading").is(":checked") && 
        !$("#chkWriting").is(":checked")) {
        $("#erSkills").text("Vui lòng chọn ít nhất một kỹ năng cần luyện");
        return false;
    }
    $("#erSkills").text("");
    return true;
}

/**
 * Update the study duration field based on selected course
 */
function updateThoiGianHoc() {
    var selectedCourse = $("#slKhoahoc option:selected");
    var duration = selectedCourse.val();
    
    // Update the thời gian học textbox
    $("#txtThoiGianHoc").val(duration + " tháng");
}

/**
 * Format date from yyyy-mm-dd to dd/mm/yyyy
 */
function formatDate(dateString) {
    if (!dateString) return '';
    const date = new Date(dateString);
    const day = date.getDate().toString().padStart(2, '0');
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const year = date.getFullYear();
    return \`\${day}/\${month}/\${year}\`;
}

/**
 * Register a new course enrollment
 * Validates all fields before proceeding
 */
function DangKy() {
    // Check all validations and store results
    var nameValid = checkName();
    var dobValid = checkDateOfBirth();
    var phoneValid = checkPhoneNum();
    var emailValid = checkEmail();
    var methodValid = checkStudyMethod();
    var skillsValid = checkSkills();
    
    // Only proceed if all validations pass
    if (!nameValid || !dobValid || !phoneValid || !emailValid || !methodValid || !skillsValid) {
        return; // Stop if any validation fails
    }

    // Gather form data
    var name = $('#txtName').val();
    var sdt = $('#txtSDT').val();
    var ngaysinh = $('#txtNgaysinh').val();
    var email = $('#txtEmail').val();
    var khoahocText = $('#slKhoahoc option:selected').text();
    var hinhthuc = $('input[name="hinhthuc"]:checked').val();
    
    // Collect selected skills
    var skills = [];
    if ($('#chkListening').is(':checked')) skills.push($('#chkListening').val());
    if ($('#chkReading').is(':checked')) skills.push($('#chkReading').val());
    if ($('#chkWriting').is(':checked')) skills.push($('#chkWriting').val());
    var skillsString = skills.join(', '); 
    
    // Format the date for display
    var formattedDate = formatDate(ngaysinh);
    
    // Add new row to the table
    var rowCount = $('#memberList tbody tr').length + 1; 
    var newRow = \`<tr>
                    <td>\${rowCount}</td>
                    <td>\${name}</td>
                    <td>\${formattedDate}</td>
                    <td>\${sdt}</td>
                    <td>\${email}</td>
                    <td>\${khoahocText}</td>
                    <td>\${hinhthuc}</td>
                    <td>\${skillsString}</td>
                  </tr>\`;
    $('#memberList tbody').append(newRow);
    
    // Hide the modal
    $('#myModal').modal('hide');
    
    // Reset form
    $('#myModal input[type="text"], #myModal input[type="email"], #myModal input[type="date"]').val('');
    $('#myModal input[type="checkbox"]').prop('checked', false);
    $('#radioCenter').prop('checked', true);
    $('#slKhoahoc').val('3');
    updateThoiGianHoc(); // Update thời gian học after resetting the form
    
    // Clear error messages
    $('#erName, #erNgaysinh, #erSDT, #erEmail, #erHinhthuc, #erSkills').text('');
}

// Initialize when the document is ready
$(document).ready(function() {
    // Add real-time validation
    $("#txtName").blur(checkName);
    $("#txtNgaysinh").blur(checkDateOfBirth);
    $("#txtSDT").blur(checkPhoneNum);
    $("#txtEmail").blur(checkEmail);
    
    // For checkboxes, validate whenever any checkbox is clicked
    $("#chkListening, #chkReading, #chkWriting").click(checkSkills);
    
    // For radios, validate whenever any radio button is clicked
    $("input[name='hinhthuc']").click(checkStudyMethod);
    
    // Set initial value for thời gian học based on default selected course
    updateThoiGianHoc();
    
    // Update thời gian học when course selection changes
    $("#slKhoahoc").change(updateThoiGianHoc);
});`;
}

/**
 * Generate CSS code for the page
 */
function generateCSSCode() {
    return `/* Base styles */
* {
    box-sizing: border-box;
    padding: 0;
    margin: 0;
    color: black;
}

body {
    font-size: 16px;
    line-height: 1.5;
}

#header {
    overflow: hidden;
}

/* Additional custom styles can be added here */
.form-check {
    margin-bottom: 5px;
}

.table th {
    background-color: #f8f9fa;
}

@media (max-width: 768px) {
    .col-3.text-right {
        text-align: left !important;
    }
}`;
}
