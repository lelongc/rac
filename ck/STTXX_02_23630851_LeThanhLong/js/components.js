/**
 * Component Library for GFree English Course Web Builder
 * This module defines the structure and templates for all available components
 */

// Base Component class with common properties and methods
class Component {
  constructor(type, name) {
    this.type = type;
    this.name = name || type.charAt(0).toUpperCase() + type.slice(1);
    this.id = `component-${type}-${Date.now()}`;
    this.classes = [];
    this.styles = {
      color: "#000000",
      backgroundColor: "#ffffff",
    };
  }

  // Method to generate a DOM element from the component
  render() {
    // Create base element
    const wrapper = document.createElement("div");
    wrapper.className = `canvas-component canvas-${this.type}`;
    wrapper.id = this.id;

    // Add custom classes
    if (this.classes.length > 0) {
      wrapper.classList.add(...this.classes);
    }

    // Apply styles
    wrapper.style.color = this.styles.color;
    wrapper.style.backgroundColor = this.styles.backgroundColor;

    // Add component content (to be overridden by child classes)
    wrapper.innerHTML = this.getTemplate();

    // Add component actions
    this.addComponentActions(wrapper);

    return wrapper;
  }

  // Add component action buttons (move up/down, delete)
  addComponentActions(element) {
    const actions = document.createElement("div");
    actions.className = "component-actions";
    actions.innerHTML = `
            <button class="btn btn-sm btn-light move-up" title="Move Up"><i class="bi bi-arrow-up"></i></button>
            <button class="btn btn-sm btn-light move-down" title="Move Down"><i class="bi bi-arrow-down"></i></button>
            <button class="btn btn-sm btn-danger delete" title="Delete"><i class="bi bi-trash"></i></button>
        `;
    element.appendChild(actions);
  }

  // Method to get component HTML template (to be implemented by child classes)
  getTemplate() {
    return "";
  }

  // Get component-specific property controls for the properties panel
  getPropertyControls() {
    return "";
  }

  // Method to update component properties
  updateProperty(property, value) {
    if (property.startsWith("style.")) {
      const styleProp = property.split(".")[1];
      this.styles[styleProp] = value;
    } else {
      this[property] = value;
    }
  }
}

// Header Component
class HeaderComponent extends Component {
  constructor() {
    super("header", "Header");
    this.logoUrl = "../image/website.png";
    this.styles.backgroundColor = "#f8f9fa";
  }

  getTemplate() {
    return `
            <div class="row" style="width: 100%">
                <img src="${this.logoUrl}" alt="Banner" style="width: 100%; height: auto; display: block" />
            </div>
        `;
  }

  getPropertyControls() {
    return `
            <div class="mb-2">
                <label for="prop-logo" class="form-label">Logo URL</label>
                <input type="text" class="form-control form-control-sm" id="prop-logo" 
                       value="${this.logoUrl}" data-property="logoUrl">
            </div>
            <div class="mb-2">
                <label for="prop-header-bg" class="form-label">Header Background</label>
                <input type="color" class="form-control form-control-sm" id="prop-header-bg" 
                       value="${this.styles.backgroundColor}" data-property="style.backgroundColor">
            </div>
        `;
  }
}

// Navigation Component
class NavigationComponent extends Component {
  constructor() {
    super("nav", "Navigation");
    this.items = [
      { text: "GFree English course", url: "#" },
      { text: "Trang chủ", url: "../html/index.html" },
      { text: "Giới thiệu", url: "#" },
      { text: "Khóa học", url: "#" },
      { text: "Web Builder", url: "../html/builder.html" },
    ];
    this.includeRegisterButton = true;
    this.registerButtonText = "Đăng ký";
    this.registerButtonClass = "btn-danger"; // Color class: btn-danger, btn-primary, etc.
    this.registerButtonSize = "btn-sm"; // Size class: btn-sm, btn-lg, etc.
    this.orientation = "horizontal"; // New property: horizontal or vertical
    this.styles.backgroundColor = "#f8f9fa";
  }

  getTemplate() {
    const navItems = this.items
      .map(
        (item) =>
          `<li class="nav-item">
                <a class="nav-link" href="${item.url}">${item.text}</a>
            </li>`
      )
      .join("");

    const registerButton = this.includeRegisterButton
      ? `<li class="nav-item">
                <button class="btn ${this.registerButtonClass} ${this.registerButtonSize} text-white" 
                        data-bs-toggle="modal" data-bs-target="#myModal">
                    ${this.registerButtonText}
                </button>
            </li>`
      : "";

    // Different template based on orientation
    if (this.orientation === "vertical") {
      return `
            <nav class="navbar navbar-expand-sm navbar-light flex-column align-items-start">
                <div class="container-fluid flex-column align-items-start p-2">
                    <ul class="navbar-nav flex-column w-100">
                        ${navItems}
                        ${registerButton}
                    </ul>
                </div>
            </nav>
        `;
    } else {
      return `
            <nav class="navbar navbar-expand-sm navbar-light">
                <div class="container-fluid">
                    <ul class="navbar-nav">
                        ${navItems}
                        ${registerButton}
                    </ul>
                </div>
            </nav>
        `;
    }
  }

  getPropertyControls() {
    return `
            <div class="mb-2">
                <label class="form-label">Navigation Properties</label>
                <p class="form-text small">Use the Navigation Links section below to manage menu items.</p>
            </div>
            
            <div class="mb-2 form-check">
                <input type="checkbox" class="form-check-input" id="include-register-btn" 
                    ${
                      this.includeRegisterButton ? "checked" : ""
                    } data-property="includeRegisterButton">
                <label class="form-check-label" for="include-register-btn">Include Register Button</label>
            </div>
            
            <div class="mb-3">
                <label for="nav-orientation" class="form-label">Navigation Orientation</label>
                <select class="form-select form-select-sm" id="nav-orientation" data-property="orientation">
                    <option value="horizontal" ${
                      this.orientation === "horizontal" ? "selected" : ""
                    }>Horizontal (Default)</option>
                    <option value="vertical" ${
                      this.orientation === "vertical" ? "selected" : ""
                    }>Vertical (Sidebar)</option>
                </select>
                <div class="form-text small mt-1">Vertical orientation is useful for sidebar navigation next to content.</div>
            </div>
        `;
  }

  updateNavItems(itemsArray) {
    this.items = itemsArray;
  }
}

// Table Component
class TableComponent extends Component {
  constructor() {
    super("table", "Table");
    this.title = "Danh sách đăng kí khóa học";
    this.columns = [
      { headerText: "STT" },
      { headerText: "Họ và tên" },
      { headerText: "Ngày sinh" },
      { headerText: "Số điện thoại" },
      { headerText: "Email" },
      { headerText: "Khóa học" },
      { headerText: "Hình thức học" },
      { headerText: "Kỹ năng cần luyện" },
    ];
    this.showBorder = true;
    this.tableId = "memberList";
  }

  getTemplate() {
    // Generate header cells from column objects
    const headerCells = this.columns
      .map((column) => {
        const headerText =
          typeof column === "string" ? column : column.headerText || "";
        return `<th>${headerText}</th>`;
      })
      .join("");

    return `
            <div class="container">
                <div class="row my-3">
                    <h3>${this.title}</h3>
                </div>
                <table class="table ${
                  this.showBorder ? "table-bordered" : ""
                }" id="${this.tableId}">
                    <thead class="bg-light">
                        <tr>
                            ${headerCells}
                        </tr>
                    </thead>
                    <tbody>
                        <!-- Registration data will be inserted here -->
                    </tbody>
                </table>
            </div>
        `;
  }

  getPropertyControls() {
    return `
            <div class="mb-2">
                <label for="prop-table-title" class="form-label">Table Title</label>
                <input type="text" class="form-control form-control-sm" id="prop-table-title" 
                       value="${this.title}" data-property="title">
            </div>
            <div class="mb-2">
                <label for="prop-table-id" class="form-label">Table ID</label>
                <input type="text" class="form-control form-control-sm" id="prop-table-id" 
                       value="${this.tableId}" data-property="tableId">
            </div>
            <div class="mb-2">
                <label class="form-label">Columns</label>
                <p class="form-text small">Use the Table Columns section below to manage columns.</p>
            </div>
        `;
  }

  updateColumns(columnsArray) {
    this.columns = columnsArray;
  }
}

// Modal Component
class ModalComponent extends Component {
  constructor() {
    super("modal", "Modal Registration");
    this.title = "THÔNG TIN ĐĂNG KÍ";
    this.modalId = "myModal";
    this.formFields = [
      { type: "text", label: "Họ và tên", id: "txtName", validation: true },
      { type: "text", label: "Số điện thoại", id: "txtSDT", validation: true },
      { type: "date", label: "Ngày sinh", id: "txtNgaysinh", validation: true },
      {
        type: "email",
        label: "Email",
        id: "txtEmail",
        placeholder: "your.email@example.com",
        validation: true,
      },
      {
        type: "select",
        label: "Khóa học",
        id: "slKhoahoc",
        options: [
          { value: "3", text: "Anh văn cơ bản", "data-name": "Anh văn cơ bản" },
          {
            value: "6",
            text: "Anh văn giao tiếp",
            "data-name": "Anh văn giao tiếp",
          },
          {
            value: "12",
            text: "Luyện thi IELTS",
            "data-name": "Luyện thi IELTS",
          },
        ],
      },
      {
        type: "text",
        label: "Thời gian học",
        id: "txtThoiGianHoc",
        readonly: true,
      },
    ];
    this.radioGroups = [
      {
        name: "hinhthuc",
        label: "Hình thức học",
        id: "radioHinhthuc",
        validation: true,
        options: [
          {
            id: "radioCenter",
            value: "Học tại trung tâm",
            label: "Học tại trung tâm",
            checked: true,
          },
          { id: "radioOnline", value: "Học online", label: "Học online" },
        ],
      },
    ];
    this.checkboxGroups = [
      {
        label: "Kỹ năng cần luyện",
        id: "chkSkills",
        validation: true,
        options: [
          { id: "chkListening", value: "Kỹ năng nghe", label: "Kỹ năng nghe" },
          { id: "chkReading", value: "Kỹ năng đọc", label: "Kỹ năng đọc" },
          { id: "chkWriting", value: "Kỹ năng viết", label: "Kỹ năng viết" },
        ],
      },
    ];
    this.registerBtnText = "Đăng kí";
    this.cancelBtnText = "Hủy";
  }

  getTemplate() {
    // This is simplified - the real modal would be much more complex
    return `
            <div class="modal fade" id="${this.modalId}" tabindex="-1" aria-labelledby="modalLabel" aria-hidden="true">
                <div class="modal-dialog modal-lg">
                    <div class="modal-content">
                        <!-- Modal header -->
                        <div class="modal-header">
                            <h2 class="modal-title" id="modalLabel">${this.title}</h2>
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                        </div>

                        <!-- Modal body with registration form -->
                        <div class="modal-body">
                            <div class="form-group">
                                <!-- Form fields will be generated here in real implementation -->
                                <div class="text-center text-muted">
                                    [Modal Registration Form with ${this.formFields.length} fields]
                                </div>
                            </div>
                        </div>

                        <!-- Modal footer -->
                        <div class="modal-footer d-flex justify-content-end">
                            <button type="button" class="btn btn-success btn-sm me-2" onclick="DangKy()">
                                ${this.registerBtnText}
                            </button>
                            <button type="button" class="btn btn-danger btn-sm" data-bs-dismiss="modal">
                                ${this.cancelBtnText}
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        `;
  }

  getPropertyControls() {
    return `
            <div class="mb-2">
                <label for="prop-modal-title" class="form-label">Modal Title</label>
                <input type="text" class="form-control form-control-sm" id="prop-modal-title" 
                       value="${this.title}" data-property="title">
            </div>
            <div class="mb-2">
                <label for="prop-modal-id" class="form-label">Modal ID</label>
                <input type="text" class="form-control form-control-sm" id="prop-modal-id" 
                       value="${this.modalId}" data-property="modalId">
            </div>
            <div class="mb-2">
                <label for="prop-register-btn" class="form-label">Register Button Text</label>
                <input type="text" class="form-control form-control-sm" id="prop-register-btn" 
                       value="${this.registerBtnText}" data-property="registerBtnText">
            </div>
            <div class="mb-2">
                <label for="prop-cancel-btn" class="form-label">Cancel Button Text</label>
                <input type="text" class="form-control form-control-sm" id="prop-cancel-btn" 
                       value="${this.cancelBtnText}" data-property="cancelBtnText">
            </div>
            <div class="mb-2">
                <label class="form-label">Form Fields</label>
                <div class="form-text mb-2 small">Form field editing available in advanced mode</div>
            </div>
        `;
  }
}

// Footer Component
class FooterComponent extends Component {
  constructor() {
    super("footer", "Footer");
    this.studentInfo = {
      name: "Lê Thanh Long",
      studentId: "23630851",
      className: "DHKTPM18A",
    };
    this.styles.backgroundColor = "#0d6efd";
    this.styles.color = "#ffffff";
  }

  getTemplate() {
    return `
            <div class="container">
                <div class="row">
                    <div class="col-12">
                        <h5 style="color: ${this.styles.color}">Thông tin sinh viên</h5>
                        <p style="color: ${this.styles.color}">Họ tên: ${this.studentInfo.name}</p>
                        <p style="color: ${this.styles.color}">Mã sinh viên: ${this.studentInfo.studentId}</p>
                        <p style="color: ${this.styles.color}">Mã lớp: ${this.studentInfo.className}</p>
                    </div>
                </div>
            </div>
        `;
  }

  getPropertyControls() {
    return `
            <div class="mb-2">
                <label for="prop-student-name" class="form-label">Student Name</label>
                <input type="text" class="form-control form-control-sm" id="prop-student-name" 
                       value="${this.studentInfo.name}" data-property="studentInfo.name">
            </div>
            <div class="mb-2">
                <label for="prop-student-id" class="form-label">Student ID</label>
                <input type="text" class="form-control form-control-sm" id="prop-student-id" 
                       value="${this.studentInfo.studentId}" data-property="studentInfo.studentId">
            </div>
            <div class="mb-2">
                <label for="prop-class-name" class="form-label">Class Name</label>
                <input type="text" class="form-control form-control-sm" id="prop-class-name" 
                       value="${this.studentInfo.className}" data-property="studentInfo.className">
            </div>
        `;
  }
}

// Image Table Layout Component
class ImageTableLayoutComponent extends Component {
  constructor() {
    super("image-table-layout", "Image + Table Layout");
    this.image = {
      url: "../image/english-class.jpg",
      altText: "English Class",
      width: "medium", // small, medium, large or pixel value
      position: "left", // left or right of table
    };
    this.table = {
      title: "Course Information",
      columns: [
        { headerText: "STT" },
        { headerText: "Họ và tên" },
        { headerText: "Ngày sinh" },
        { headerText: "Số điện thoại" },
        { headerText: "Email" },
        { headerText: "Khóa học" },
      ],
      showBorder: true,
      tableId: "imageTableData",
    };
    this.columnClasses = {
      imageCol: "col-md-4",
      tableCol: "col-md-8",
    };
  }

  getTemplate() {
    // Generate columns in proper order based on image position
    const imageColumnHtml = `
        <div class="${this.columnClasses.imageCol} text-center">
            <img src="${this.image.url}" alt="${this.image.altText}" 
                 class="img-fluid rounded ${
                   this.image.width === "small"
                     ? "w-50"
                     : this.image.width === "medium"
                     ? "w-75"
                     : this.image.width === "large"
                     ? "w-100"
                     : ""
                 }" 
                 ${
                   this.image.width &&
                   !["small", "medium", "large"].includes(this.image.width)
                     ? `style="width:${this.image.width}px"`
                     : ""
                 }>
        </div>`;

    // Generate header cells from column objects - match the TableComponent format
    const headerCells = this.table.columns
      .map((column) => {
        const headerText =
          typeof column === "string" ? column : column.headerText || "";
        return `<th>${headerText}</th>`;
      })
      .join("");

    const tableColumnHtml = `
        <div class="${this.columnClasses.tableCol}">
            <h3>${this.table.title}</h3>
            <table class="table ${
              this.table.showBorder ? "table-bordered" : ""
            }" id="${this.table.tableId}">
                <thead class="bg-light">
                    <tr>
                        ${headerCells}
                    </tr>
                </thead>
                <tbody>
                    <!-- Table data will be inserted here -->
                </tbody>
            </table>
        </div>`;

    // Arrange columns based on image position
    return `
        <div class="container">
            <div class="row align-items-center">
                ${
                  this.image.position === "left"
                    ? imageColumnHtml + tableColumnHtml
                    : tableColumnHtml + imageColumnHtml
                }
            </div>
        </div>
    `;
  }

  getPropertyControls() {
    return `
        <div class="mb-2">
            <label for="prop-image-url" class="form-label">Image URL</label>
            <input type="text" class="form-control form-control-sm" id="prop-image-url" 
                value="${this.image.url}" data-property="image.url">
        </div>
        
        <div class="mb-2">
            <label for="prop-image-alt" class="form-label">Image Alt Text</label>
            <input type="text" class="form-control form-control-sm" id="prop-image-alt" 
                value="${this.image.altText}" data-property="image.altText">
        </div>
        
        <div class="mb-2">
            <label for="prop-image-width" class="form-label">Image Size</label>
            <select class="form-select form-select-sm" id="prop-image-width" data-property="image.width">
                <option value="small" ${
                  this.image.width === "small" ? "selected" : ""
                }>Small (50%)</option>
                <option value="medium" ${
                  this.image.width === "medium" ? "selected" : ""
                }>Medium (75%)</option>
                <option value="large" ${
                  this.image.width === "large" ? "selected" : ""
                }>Large (100%)</option>
                <option value="200" ${
                  this.image.width === "200" ? "selected" : ""
                }>Custom: 200px</option>
                <option value="300" ${
                  this.image.width === "300" ? "selected" : ""
                }>Custom: 300px</option>
            </select>
        </div>
        
        <div class="mb-3">
            <label class="form-label d-block">Image Position</label>
            <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="imagePosition" id="pos-left"
                    value="left" ${
                      this.image.position === "left" ? "checked" : ""
                    } data-property="image.position">
                <label class="form-check-label" for="pos-left">Left of Table</label>
            </div>
            <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="imagePosition" id="pos-right"
                    value="right" ${
                      this.image.position === "right" ? "checked" : ""
                    } data-property="image.position">
                <label class="form-check-label" for="pos-right">Right of Table</label>
            </div>
        </div>
        
        <div class="mb-2">
            <label class="form-label">Layout Distribution</label>
            <select class="form-select form-select-sm" id="prop-column-ratio" data-property="columnRatio">
                <option value="4-8" ${
                  this.columnClasses.imageCol === "col-md-4" ? "selected" : ""
                }>Image: 1/3, Table: 2/3</option>
                <option value="5-7" ${
                  this.columnClasses.imageCol === "col-md-5" ? "selected" : ""
                }>Image: 5/12, Table: 7/12</option>
                <option value="6-6" ${
                  this.columnClasses.imageCol === "col-md-6" ? "selected" : ""
                }>Image: 1/2, Table: 1/2</option>
                <option value="7-5" ${
                  this.columnClasses.imageCol === "col-md-7" ? "selected" : ""
                }>Image: 7/12, Table: 5/12</option>
                <option value="8-4" ${
                  this.columnClasses.imageCol === "col-md-8" ? "selected" : ""
                }>Image: 2/3, Table: 1/3</option>
            </select>
        </div>
        
        <div class="mb-2">
            <label for="prop-table-title" class="form-label">Table Title</label>
            <input type="text" class="form-control form-control-sm" id="prop-table-title" 
                value="${this.table.title}" data-property="table.title">
        </div>
        
        <div class="mb-2 form-check">
            <input class="form-check-input" type="checkbox" id="show-table-border" 
                ${
                  this.table.showBorder ? "checked" : ""
                } data-property="table.showBorder">
            <label class="form-check-label" for="show-table-border">Show Table Border</label>
        </div>
        
        <div class="mb-2">
            <label class="form-label">Table Columns</label>
            <p class="form-text small">Use the Table Columns section below to manage columns.</p>
        </div>
    `;
  }

  // Handle special property updates that impact multiple sub-properties
  updateProperty(property, value) {
    if (property === "columnRatio") {
      // Special case for column ratio which affects both column classes
      switch (value) {
        case "4-8":
          this.columnClasses.imageCol = "col-md-4";
          this.columnClasses.tableCol = "col-md-8";
          break;
        case "5-7":
          this.columnClasses.imageCol = "col-md-5";
          this.columnClasses.tableCol = "col-md-7";
          break;
        case "6-6":
          this.columnClasses.imageCol = "col-md-6";
          this.columnClasses.tableCol = "col-md-6";
          break;
        case "7-5":
          this.columnClasses.imageCol = "col-md-7";
          this.columnClasses.tableCol = "col-md-5";
          break;
        case "8-4":
          this.columnClasses.imageCol = "col-md-8";
          this.columnClasses.tableCol = "col-md-4";
          break;
      }
    } else {
      // For all other properties, use the default implementation
      super.updateProperty(property, value);
    }
  }
}

// NEW COMPONENT: Nav + Table Layout Component
class NavTableLayoutComponent extends Component {
  constructor() {
    super("nav-table-layout", "Nav + Table Layout");
    this.navigation = {
      items: [
        { text: "GFree English", url: "#" },
        { text: "Trang chủ", url: "../html/index.html" },
        { text: "Giới thiệu", url: "#" },
        { text: "Khóa học", url: "#" },
        { text: "Web Builder", url: "../html/builder.html" },
      ],
      includeRegisterButton: true,
      registerButtonText: "Đăng ký",
      registerButtonClass: "btn-danger",
      registerButtonSize: "btn-sm",
      position: "left", // left or right of table
    };
    this.table = {
      title: "Danh sách đăng kí khóa học",
      columns: [
        { headerText: "STT" },
        { headerText: "Họ và tên" },
        { headerText: "Ngày sinh" },
        { headerText: "Số điện thoại" },
        { headerText: "Email" },
        { headerText: "Khóa học" },
      ],
      showBorder: true,
      tableId: "navTableData",
    };
    this.columnClasses = {
      navCol: "col-md-3",
      tableCol: "col-md-9",
    };
  }

  getTemplate() {
    // Generate nav items HTML from the items array
    const navItems = this.navigation.items
      .map(
        (item) => `
          <li class="nav-item">
              <a class="nav-link" href="${item.url || "#"}">${
          item.text || "Link"
        }</a>
          </li>`
      )
      .join("\n");

    // Add register button if enabled
    const registerButton = this.navigation.includeRegisterButton
      ? `
          <li class="nav-item mt-2">
              <button class="btn ${this.navigation.registerButtonClass} ${this.navigation.registerButtonSize} text-white" 
                      data-bs-toggle="modal" data-bs-target="#myModal">
                  ${this.navigation.registerButtonText}
              </button>
          </li>`
      : "";

    // Create vertical navigation column
    const navColumnHtml = `
        <div class="${this.columnClasses.navCol}">
            <nav class="navbar navbar-expand-sm navbar-light flex-column align-items-start">
                <div class="container-fluid flex-column align-items-start p-2">
                    <ul class="navbar-nav flex-column w-100">
                        ${navItems}
                        ${registerButton}
                    </ul>
                </div>
            </nav>
        </div>`;

    // Generate header cells from column objects
    const headerCells = this.table.columns
      .map((column) => {
        const headerText =
          typeof column === "string" ? column : column.headerText || "";
        return `<th>${headerText}</th>`;
      })
      .join("");

    // Create table column
    const tableColumnHtml = `
        <div class="${this.columnClasses.tableCol}">
            <h3>${this.table.title}</h3>
            <table class="table ${
              this.table.showBorder ? "table-bordered" : ""
            }" id="${this.table.tableId}">
                <thead class="bg-light">
                    <tr>
                        ${headerCells}
                    </tr>
                </thead>
                <tbody>
                    <!-- Table data will be inserted here -->
                </tbody>
            </table>
        </div>`;

    // Arrange columns based on navigation position
    return `
        <div class="container">
            <div class="row">
                ${
                  this.navigation.position === "left"
                    ? navColumnHtml + tableColumnHtml
                    : tableColumnHtml + navColumnHtml
                }
            </div>
        </div>
    `;
  }

  getPropertyControls() {
    return `
        <div class="mb-3">
            <h6 class="border-bottom pb-2">Navigation Settings</h6>
            <div class="mb-2 form-check">
                <input type="checkbox" class="form-check-input" id="include-register-btn" 
                    ${
                      this.navigation.includeRegisterButton ? "checked" : ""
                    } data-property="navigation.includeRegisterButton">
                <label class="form-check-label" for="include-register-btn">Include Register Button</label>
            </div>
            
            <div class="mb-2">
                <label for="register-btn-text" class="form-label">Button Text</label>
                <input type="text" class="form-control form-control-sm" id="register-btn-text" 
                    value="${
                      this.navigation.registerButtonText
                    }" data-property="navigation.registerButtonText">
            </div>
            
            <div class="mb-3">
                <label class="form-label d-block">Navigation Position</label>
                <div class="form-check form-check-inline">
                    <input class="form-check-input" type="radio" name="navPosition" id="nav-left"
                        value="left" ${
                          this.navigation.position === "left" ? "checked" : ""
                        } data-property="navigation.position">
                    <label class="form-check-label" for="nav-left">Left of Table</label>
                </div>
                <div class="form-check form-check-inline">
                    <input class="form-check-input" type="radio" name="navPosition" id="nav-right"
                        value="right" ${
                          this.navigation.position === "right" ? "checked" : ""
                        } data-property="navigation.position">
                    <label class="form-check-label" for="nav-right">Right of Table</label>
                </div>
            </div>
        </div>

        <div class="mb-3">
            <h6 class="border-bottom pb-2">Table Settings</h6>
            <div class="mb-2">
                <label for="prop-table-title" class="form-label">Table Title</label>
                <input type="text" class="form-control form-control-sm" id="prop-table-title" 
                    value="${this.table.title}" data-property="table.title">
            </div>
            
            <div class="mb-2">
                <label class="form-label">Layout Distribution</label>
                <select class="form-select form-select-sm" id="prop-column-ratio" data-property="columnRatio">
                    <option value="3-9" ${
                      this.columnClasses.navCol === "col-md-3" ? "selected" : ""
                    }>Nav: 1/4, Table: 3/4</option>
                    <option value="4-8" ${
                      this.columnClasses.navCol === "col-md-4" ? "selected" : ""
                    }>Nav: 1/3, Table: 2/3</option>
                    <option value="5-7" ${
                      this.columnClasses.navCol === "col-md-5" ? "selected" : ""
                    }>Nav: 5/12, Table: 7/12</option>
                </select>
            </div>

            <div class="mb-2 form-check">
                <input class="form-check-input" type="checkbox" id="show-table-border" 
                    ${
                      this.table.showBorder ? "checked" : ""
                    } data-property="table.showBorder">
                <label class="form-check-label" for="show-table-border">Show Table Border</label>
            </div>

            <div class="mb-2">
                <label class="form-label">Menu and Table Content</label>
                <p class="form-text small">Use the Navigation and Table sections below to manage items and columns.</p>
            </div>
        </div>
    `;
  }

  // Handle special property updates that impact multiple sub-properties
  updateProperty(property, value) {
    if (property === "columnRatio") {
      // Special case for column ratio which affects both column classes
      switch (value) {
        case "3-9":
          this.columnClasses.navCol = "col-md-3";
          this.columnClasses.tableCol = "col-md-9";
          break;
        case "4-8":
          this.columnClasses.navCol = "col-md-4";
          this.columnClasses.tableCol = "col-md-8";
          break;
        case "5-7":
          this.columnClasses.navCol = "col-md-5";
          this.columnClasses.tableCol = "col-md-7";
          break;
      }
    } else {
      // For all other properties, use the default implementation
      super.updateProperty(property, value);
    }
  }
}

// Component Factory - creates components by type
class ComponentFactory {
  static createComponent(type) {
    switch (type) {
      case "header":
        return new HeaderComponent();
      case "nav":
        return new NavigationComponent();
      case "table":
        return new TableComponent();
      case "modal":
        return new ModalComponent();
      case "footer":
        return new FooterComponent();
      case "image-table-layout":
        return new ImageTableLayoutComponent();
      case "nav-table-layout":
        return new NavTableLayoutComponent();
      default:
        throw new Error(`Unknown component type: ${type}`);
    }
  }

  static getComponentTypes() {
    return [
      { type: "header", name: "Header", icon: "bi-image" },
      { type: "nav", name: "Navigation", icon: "bi-menu-button-wide" },
      { type: "table", name: "Table", icon: "bi-table" },
      {
        type: "image-table-layout",
        name: "Image+Table Layout",
        icon: "bi-layout-split",
      },
      {
        type: "nav-table-layout",
        name: "Nav+Table Layout",
        icon: "bi-layout-sidebar",
      },
      { type: "modal", name: "Modal Registration", icon: "bi-window" },
      { type: "footer", name: "Footer", icon: "bi-layout-text-window-reverse" },
    ];
  }
}

// Export the component classes
window.ComponentLibrary = {
  Component,
  HeaderComponent,
  NavigationComponent,
  TableComponent,
  ModalComponent,
  FooterComponent,
  ImageTableLayoutComponent,
  NavTableLayoutComponent,
  ComponentFactory,
};
