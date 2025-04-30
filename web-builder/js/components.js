/**
 * Component creation functions
 */

/**
 * Create banner component
 */
function createBannerComponent(id) {
  return $(`
        <div id="${id}" class="canvas-component" data-type="banner">
            <div class="component-actions">
                <button type="button" class="drag-handle" title="Drag to move"><i class="fas fa-arrows-alt"></i></button>
                <button type="button" class="move-up-btn" title="Move up"><i class="fas fa-arrow-up"></i></button>
                <button type="button" class="move-down-btn" title="Move down"><i class="fas fa-arrow-down"></i></button>
                <button type="button" class="duplicate-btn" title="Duplicate"><i class="fas fa-copy"></i></button>
                <button type="button" class="delete-btn" title="Delete"><i class="fas fa-trash"></i></button>
            </div>
            <div id="header" style="width: 100%;">
                <div class="row" style="width: 100%;">
                    <img src="https://via.placeholder.com/800x200?text=Banner+Image" alt="Banner" style="width: 100%; height: auto; display: block;">
                </div>
            </div>
        </div>
    `);
}

/**
 * Create navbar component
 */
function createNavbarComponent(id) {
  return $(`
        <div id="${id}" class="canvas-component" data-type="navbar">
            <div class="component-actions">
                <button type="button" class="drag-handle" title="Drag to move"><i class="fas fa-arrows-alt"></i></button>
                <button type="button" class="move-up-btn" title="Move up"><i class="fas fa-arrow-up"></i></button>
                <button type="button" class="move-down-btn" title="Move down"><i class="fas fa-arrow-down"></i></button>
                <button type="button" class="duplicate-btn" title="Duplicate"><i class="fas fa-copy"></i></button>
                <button type="button" class="delete-btn" title="Delete"><i class="fas fa-trash"></i></button>
            </div>
            <div id="navbar">
                <nav class="navbar navbar-expand-sm navbar-light bg-light">
                    <div class="container-fluid">
                        <ul class="navbar-nav">
                            <li class="nav-item">
                                <a class="nav-link" href="#">GFree English course</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#">Trang chủ</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#">Giới thiệu</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#">Khóa học</a>
                            </li>
                            <li class="nav-item">
                                <button class="btn btn-danger text-white btn-sm" data-bs-toggle="modal" data-bs-target="#myModal">Đăng ký</button>
                            </li>
                        </ul>
                    </div>
                </nav>
            </div>
        </div>
    `);
}

/**
 * Create table component
 */
function createTableComponent(id) {
  return $(`
        <div id="${id}" class="canvas-component" data-type="table">
            <div class="component-actions">
                <button type="button" class="drag-handle" title="Drag to move"><i class="fas fa-arrows-alt"></i></button>
                <button type="button" class="move-up-btn" title="Move up"><i class="fas fa-arrow-up"></i></button>
                <button type="button" class="move-down-btn" title="Move down"><i class="fas fa-arrow-down"></i></button>
                <button type="button" class="duplicate-btn" title="Duplicate"><i class="fas fa-copy"></i></button>
                <button type="button" class="delete-btn" title="Delete"><i class="fas fa-trash"></i></button>
            </div>
            <div class="container">
                <div class="row my-3">
                    <h3>Danh sách đăng kí khóa học</h3>
                </div>
                <table class="table table-bordered" id="memberList">
                    <thead class="bg-light">
                        <tr>
                            <th>STT</th>
                            <th>Họ và tên</th>
                            <th>Ngày sinh</th>
                            <th>Số điện thoại</th>
                            <th>Email</th>
                            <th>Khóa học</th>
                            <th>Hình thức học</th>
                            <th>Kỹ năng cần luyện</th>
                        </tr>
                    </thead>
                    <tbody>
                        <!-- Registration data will be inserted here -->
                    </tbody>
                </table>
            </div>
        </div>
    `);
}

/**
 * Create text field component
 */
function createTextFieldComponent(id) {
  return $(`
        <div id="${id}" class="canvas-component" data-type="text-field">
            <div class="component-actions">
                <button type="button" class="drag-handle" title="Drag to move"><i class="fas fa-arrows-alt"></i></button>
                <button type="button" class="move-up-btn" title="Move up"><i class="fas fa-arrow-up"></i></button>
                <button type="button" class="move-down-btn" title="Move down"><i class="fas fa-arrow-down"></i></button>
                <button type="button" class="duplicate-btn" title="Duplicate"><i class="fas fa-copy"></i></button>
                <button type="button" class="delete-btn" title="Delete"><i class="fas fa-trash"></i></button>
            </div>
            <div class="row mt-2">
                <div class="col-3 text-right">
                    <label for="txtField${id}" class="font-weight-normal">Trường nhập liệu</label>
                </div>
                <div class="col-9">
                    <input type="text" id="txtField${id}" class="form-control">
                    <span id="erField${id}" class="text-danger small mt-1 d-block"></span>
                </div>
            </div>
        </div>
    `);
}

/**
 * Create email field component
 */
function createEmailFieldComponent(id) {
  return $(`
        <div id="${id}" class="canvas-component" data-type="email-field">
            <div class="component-actions">
                <button type="button" class="drag-handle" title="Drag to move"><i class="fas fa-arrows-alt"></i></button>
                <button type="button" class="move-up-btn" title="Move up"><i class="fas fa-arrow-up"></i></button>
                <button type="button" class="move-down-btn" title="Move down"><i class="fas fa-arrow-down"></i></button>
                <button type="button" class="duplicate-btn" title="Duplicate"><i class="fas fa-copy"></i></button>
                <button type="button" class="delete-btn" title="Delete"><i class="fas fa-trash"></i></button>
            </div>
            <div class="row mt-2">
                <div class="col-3 text-right">
                    <label for="txtEmail${id}" class="font-weight-normal">Email</label>
                </div>
                <div class="col-9">
                    <input type="email" id="txtEmail${id}" class="form-control" placeholder="your.email@example.com">
                    <span id="erEmail${id}" class="text-danger small mt-1 d-block"></span>
                </div>
            </div>
        </div>
    `);
}

/**
 * Create date field component
 */
function createDateFieldComponent(id) {
  return $(`
        <div id="${id}" class="canvas-component" data-type="date-field">
            <div class="component-actions">
                <button type="button" class="drag-handle" title="Drag to move"><i class="fas fa-arrows-alt"></i></button>
                <button type="button" class="move-up-btn" title="Move up"><i class="fas fa-arrow-up"></i></button>
                <button type="button" class="move-down-btn" title="Move down"><i class="fas fa-arrow-down"></i></button>
                <button type="button" class="duplicate-btn" title="Duplicate"><i class="fas fa-copy"></i></button>
                <button type="button" class="delete-btn" title="Delete"><i class="fas fa-trash"></i></button>
            </div>
            <div class="row mt-2">
                <div class="col-3 text-right">
                    <label for="txtDate${id}" class="font-weight-normal">Ngày sinh</label>
                </div>
                <div class="col-9">
                    <input type="date" id="txtDate${id}" class="form-control">
                    <span id="erDate${id}" class="text-danger small mt-1 d-block"></span>
                </div>
            </div>
        </div>
    `);
}

/**
 * Create select dropdown component
 */
function createSelectComponent(id) {
  return $(`
        <div id="${id}" class="canvas-component" data-type="select">
            <div class="component-actions">
                <button type="button" class="drag-handle" title="Drag to move"><i class="fas fa-arrows-alt"></i></button>
                <button type="button" class="move-up-btn" title="Move up"><i class="fas fa-arrow-up"></i></button>
                <button type="button" class="move-down-btn" title="Move down"><i class="fas fa-arrow-down"></i></button>
                <button type="button" class="duplicate-btn" title="Duplicate"><i class="fas fa-copy"></i></button>
                <button type="button" class="delete-btn" title="Delete"><i class="fas fa-trash"></i></button>
            </div>
            <div class="row mt-2">
                <div class="col-3 text-right">
                    <label for="slSelect${id}" class="font-weight-normal">Khóa học</label>
                </div>
                <div class="col-9">
                    <select id="slSelect${id}" class="form-control">
                        <option value="3" data-name="Anh văn cơ bản">Anh văn cơ bản</option>
                        <option value="6" data-name="Anh văn giao tiếp">Anh văn giao tiếp</option>
                        <option value="12" data-name="Luyện thi IELTS">Luyện thi IELTS</option>
                    </select>
                </div>
            </div>
        </div>
    `);
}

/**
 * Create radio group component
 */
function createRadioGroupComponent(id) {
  return $(`
        <div id="${id}" class="canvas-component" data-type="radio-group">
            <div class="component-actions">
                <button type="button" class="drag-handle" title="Drag to move"><i class="fas fa-arrows-alt"></i></button>
                <button type="button" class="move-up-btn" title="Move up"><i class="fas fa-arrow-up"></i></button>
                <button type="button" class="move-down-btn" title="Move down"><i class="fas fa-arrow-down"></i></button>
                <button type="button" class="duplicate-btn" title="Duplicate"><i class="fas fa-copy"></i></button>
                <button type="button" class="delete-btn" title="Delete"><i class="fas fa-trash"></i></button>
            </div>
            <div class="row mt-2">
                <div class="col-3 text-right">
                    <label class="font-weight-normal">Hình thức học</label>
                </div>
                <div class="col-9">
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="hinhthuc${id}" id="radio1${id}" value="Học tại trung tâm" checked>
                        <label class="form-check-label" for="radio1${id}">Học tại trung tâm</label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="radio" name="hinhthuc${id}" id="radio2${id}" value="Học online">
                        <label class="form-check-label" for="radio2${id}">Học online</label>
                    </div>
                    <span id="erRadio${id}" class="text-danger small mt-1 d-block"></span>
                </div>
            </div>
        </div>
    `);
}

/**
 * Create checkbox group component
 */
function createCheckboxGroupComponent(id) {
  return $(`
        <div id="${id}" class="canvas-component" data-type="checkbox-group">
            <div class="component-actions">
                <button type="button" class="drag-handle" title="Drag to move"><i class="fas fa-arrows-alt"></i></button>
                <button type="button" class="move-up-btn" title="Move up"><i class="fas fa-arrow-up"></i></button>
                <button type="button" class="move-down-btn" title="Move down"><i class="fas fa-arrow-down"></i></button>
                <button type="button" class="duplicate-btn" title="Duplicate"><i class="fas fa-copy"></i></button>
                <button type="button" class="delete-btn" title="Delete"><i class="fas fa-trash"></i></button>
            </div>
            <div class="row mt-2">
                <div class="col-3 text-right">
                    <label class="font-weight-normal">Kỹ năng cần luyện</label>
                </div>
                <div class="col-9">
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="chk1${id}" value="Kỹ năng nghe">
                        <label class="form-check-label" for="chk1${id}">Kỹ năng nghe</label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="chk2${id}" value="Kỹ năng đọc">
                        <label class="form-check-label" for="chk2${id}">Kỹ năng đọc</label>
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="chk3${id}" value="Kỹ năng viết">
                        <label class="form-check-label" for="chk3${id}">Kỹ năng viết</label>
                    </div>
                    <span id="erCheck${id}" class="text-danger small mt-1 d-block"></span>
                </div>
            </div>
        </div>
    `);
}

/**
 * Create modal component
 */
function createModalComponent(id) {
  const defaultFields = [
    {
      type: "text-field",
      label: "Họ và tên",
      id: "txtName",
      required: true,
      placeholder: "",
      validation: {
        regex: "^[A-Z][a-z]*(\\s+[A-Z][a-z]*)+$",
        message: "Mỗi từ phải bắt đầu bằng chữ hoa và phần còn lại viết thường",
        function: "checkName",
      },
    },
    {
      type: "text-field",
      label: "Số điện thoại",
      id: "txtSDT",
      required: true,
      placeholder: "",
      validation: {
        regex: "^(09|03|08)\\d{8}$",
        message: "Số điện thoại phải có 10 số và bắt đầu với 09, 03 hoặc 08",
        function: "checkPhoneNum",
      },
    },
    {
      type: "date-field",
      label: "Ngày sinh",
      id: "txtNgaysinh",
      required: true,
      validation: {
        function: "checkDateOfBirth",
      },
    },
    {
      type: "email-field",
      label: "Email",
      id: "txtEmail",
      required: true,
      placeholder: "your.email@example.com",
      validation: {
        regex: "@.*\\.com$",
        message: "Email phải chứa @ và kết thúc với .com",
        function: "checkEmail",
      },
    },
    {
      type: "select",
      label: "Khóa học",
      id: "slKhoahoc",
      required: true,
      options: [
        { value: "3", text: "Anh văn cơ bản" },
        { value: "6", text: "Anh văn giao tiếp" },
        { value: "12", text: "Luyện thi IELTS" },
      ],
    },
    {
      type: "readonly-field",
      label: "Thời gian học",
      id: "txtThoiGianHoc",
      required: false,
      readonly: true,
    },
    {
      type: "radio-group",
      label: "Hình thức học",
      name: "hinhthuc",
      required: true,
      options: [
        {
          id: "radioCenter",
          value: "Học tại trung tâm",
          text: "Học tại trung tâm",
          checked: true,
        },
        { id: "radioOnline", value: "Học online", text: "Học online" },
      ],
      validation: {
        function: "checkStudyMethod",
      },
    },
    {
      type: "checkbox-group",
      label: "Kỹ năng cần luyện",
      id: "chkSkills",
      required: true,
      options: [
        { id: "chkListening", value: "Kỹ năng nghe", text: "Kỹ năng nghe" },
        { id: "chkReading", value: "Kỹ năng đọc", text: "Kỹ năng đọc" },
        { id: "chkWriting", value: "Kỹ năng viết", text: "Kỹ năng viết" },
      ],
      validation: {
        function: "checkSkills",
      },
    },
  ];

  // Create the modal component
  const component = $(`
    <div id="${id}" class="canvas-component" data-type="modal">
      <div class="component-actions">
          <button type="button" class="drag-handle" title="Drag to move"><i class="fas fa-arrows-alt"></i></button>
          <button type="button" class="move-up-btn" title="Move up"><i class="fas fa-arrow-up"></i></button>
          <button type="button" class="move-down-btn" title="Move down"><i class="fas fa-arrow-down"></i></button>
          <button type="button" class="duplicate-btn" title="Duplicate"><i class="fas fa-copy"></i></button>
          <button type="button" class="delete-btn" title="Delete"><i class="fas fa-trash"></i></button>
      </div>
      <div class="p-3 bg-light border" style="position: relative;">
          <div style="text-align: center; margin-bottom: 10px;">
              <i class="fas fa-window-restore mr-2"></i> 
              <span class="modal-preview-title">Form Modal: THÔNG TIN ĐĂNG KÍ</span>
              <div class="small text-muted">Modal sẽ xuất hiện khi người dùng nhấn nút đăng ký</div>
          </div>
          <div class="modal-preview-fields" style="font-size: 12px; color: #666;">
              <!-- Fields will be inserted here dynamically -->
          </div>
          <div class="mt-2 d-flex justify-content-between">
              <button class="btn btn-sm btn-primary edit-modal-btn">
                  <i class="fas fa-cog"></i> Cài đặt chung
              </button>
              <button class="btn btn-sm btn-success edit-modal-fields-btn">
                  <i class="fas fa-edit"></i> Chỉnh sửa trường
              </button>
          </div>
      </div>
    </div>
  `);

  // Store fields data in component's data
  component.data("fields", defaultFields);
  component.data("modal-id", "myModal");
  component.data("modal-title", "THÔNG TIN ĐĂNG KÍ");
  component.data("modal-size", "modal-lg");
  component.data("submit-text", "Đăng kí");
  component.data("cancel-text", "Hủy");

  // Generate preview fields
  updateModalPreviewFields(component);

  return component;
}

/**
 * Helper function to update the modal preview fields
 */
function updateModalPreviewFields(component) {
  const fields = component.data("fields");
  const previewContainer = component.find(".modal-preview-fields");

  // Clear previous content
  previewContainer.empty();

  // Add each field to the preview
  fields.forEach((field) => {
    let fieldType = "";
    switch (field.type) {
      case "text-field":
        fieldType = "Text";
        break;
      case "email-field":
        fieldType = "Email";
        break;
      case "date-field":
        fieldType = "Date";
        break;
      case "select":
        fieldType = "Select";
        break;
      case "radio-group":
        fieldType = "Radio";
        break;
      case "checkbox-group":
        fieldType = "Checkbox";
        break;
      case "readonly-field":
        fieldType = "Text (readonly)";
        break;
      default:
        fieldType = field.type;
    }

    let validationInfo = "";
    if (field.validation && field.validation.regex) {
      validationInfo = ` <span class="text-info small">[Regex]</span>`;
    }

    const requiredMark = field.required
      ? ' <span class="text-danger">*</span>'
      : "";
    previewContainer.append(
      `<div>- ${field.label}${requiredMark} (${fieldType})${validationInfo}</div>`
    );
  });
}

/**
 * Create button component
 */
function createButtonComponent(id) {
  return $(`
        <div id="${id}" class="canvas-component" data-type="button">
            <div class="component-actions">
                <button type="button" class="drag-handle" title="Drag to move"><i class="fas fa-arrows-alt"></i></button>
                <button type="button" class="move-up-btn" title="Move up"><i class="fas fa-arrow-up"></i></button>
                <button type="button" class="move-down-btn" title="Move down"><i class="fas fa-arrow-down"></i></button>
                <button type="button" class="duplicate-btn" title="Duplicate"><i class="fas fa-copy"></i></button>
                <button type="button" class="delete-btn" title="Delete"><i class="fas fa-trash"></i></button>
            </div>
            <div class="row mt-2">
                <div class="col-3 text-right">
                    <label class="font-weight-normal">Nút</label>
                </div>
                <div class="col-9">
                    <button type="button" class="btn btn-success">Đăng ký</button>
                </div>
            </div>
        </div>
    `);
}

/**
 * Create footer component
 */
function createFooterComponent(id) {
  return $(`
        <div id="${id}" class="canvas-component" data-type="footer">
            <div class="component-actions">
                <button type="button" class="drag-handle" title="Drag to move"><i class="fas fa-arrows-alt"></i></button>
                <button type="button" class="move-up-btn" title="Move up"><i class="fas fa-arrow-up"></i></button>
                <button type="button" class="move-down-btn" title="Move down"><i class="fas fa-arrow-down"></i></button>
                <button type="button" class="duplicate-btn" title="Duplicate"><i class="fas fa-copy"></i></button>
                <button type="button" class="delete-btn" title="Delete"><i class="fas fa-trash"></i></button>
            </div>
            <div id="footer" style="background-color: #007bff; color: white; padding: 20px 0; margin-top: 20px; text-align: center;">
                <div class="container">
                    <div class="row">
                        <div class="col-12">
                            <h5 style="color: white;">Thông tin sinh viên</h5>
                            <p style="color: white; margin: 5px 0;">Họ tên: Lê Thanh Long</p>
                            <p style="color: white; margin: 5px 0;">Mã sinh viên: 23630851</p>
                            <p style="color: white; margin: 5px 0;">Mã lớp: DHKTPM18A</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `);
}
