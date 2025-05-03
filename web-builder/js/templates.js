/**
 * Template presets for the Web Builder
 * Contains predefined templates based on example files
 */

// Template configuration
const templates = {
  // Template 1: English Course Registration (based on ck/4)
  "english-course": {
    title: "GFree English Course Registration",
    headerBgColor: "#0d6efd",
    headerTextColor: "#ffffff",
    formBgColor: "#ffffff",
    formBorderColor: "#000000",
    footerBgColor: "#0d6efd",
    footerTextColor: "#ffffff",
    footerText: "MSSV: 23630851 | Họ tên: Lê Thanh Long | Mã lớp: DHKTPM18A",
    fields: [
      {
        type: "text",
        label: "Họ và tên",
        name: "txtName",
        placeholder: "Nhập họ và tên",
        regex: "^[A-Z][a-z]*(\\s+[A-Z][a-z]*)+$",
        errorMessage:
          "Mỗi từ phải bắt đầu bằng chữ hoa và phần còn lại viết thường",
        required: true,
      },
      {
        type: "tel",
        label: "Số điện thoại",
        name: "txtSDT",
        placeholder: "Nhập số điện thoại",
        regex: "^(09|03|08)\\d{8}$",
        errorMessage:
          "Số điện thoại phải có 10 số và bắt đầu với 09, 03 hoặc 08",
        required: true,
      },
      {
        type: "date",
        label: "Ngày sinh",
        name: "txtNgaysinh",
        placeholder: "",
        regex: "",
        errorMessage: "Ngày sinh phải trước ngày hiện tại",
        required: true,
        validateFunction: "checkDateOfBirth",
      },
      {
        type: "email",
        label: "Email",
        name: "txtEmail",
        placeholder: "your.email@example.com",
        regex: "@.*\\.com$",
        errorMessage: "Email phải chứa @ và kết thúc với .com",
        required: true,
      },
      {
        type: "select",
        label: "Khóa học",
        name: "slKhoahoc",
        options: [
          { value: "3", label: "Anh văn cơ bản" },
          { value: "6", label: "Anh văn giao tiếp" },
          { value: "12", label: "Luyện thi IELTS" },
        ],
        required: true,
      },
      {
        type: "radio",
        label: "Hình thức học",
        name: "hinhthuc",
        options: [
          { value: "Học tại trung tâm", label: "Học tại trung tâm" },
          { value: "Học online", label: "Học online" },
        ],
        required: true,
      },
      {
        type: "checkbox",
        label: "Kỹ năng cần luyện",
        name: "skills",
        options: [
          { value: "Kỹ năng nghe", label: "Kỹ năng nghe" },
          { value: "Kỹ năng đọc", label: "Kỹ năng đọc" },
          { value: "Kỹ năng viết", label: "Kỹ năng viết" },
        ],
        required: true,
      },
    ],
    tableHeaders: [
      "STT",
      "Họ và tên",
      "Ngày sinh",
      "Số điện thoại",
      "Email",
      "Khóa học",
      "Hình thức học",
      "Kỹ năng cần luyện",
    ],
  },

  // Template 2: Flower Shop Order Form (based on ck/3)
  "flower-order": {
    title: "Đặt Mua Hoa",
    headerBgColor: "#ffffff",
    headerTextColor: "#000000",
    formBgColor: "#ffffff",
    formBorderColor: "#000000",
    footerBgColor: "#ffffff",
    footerTextColor: "#000000",
    footerText: "MSSV: 23630851 | Lê Thành Long",
    fields: [
      {
        type: "text",
        label: "Họ Và Tên",
        name: "name",
        placeholder: "Nhập họ và tên",
        regex: "^[A-Z][a-z]+(\\s[A-Z][a-z]+)+$",
        errorMessage: "Họ và tên không hợp lệ!",
        required: true,
      },
      {
        type: "tel",
        label: "Số Điện Thoại",
        name: "phone",
        placeholder: "Nhập số điện thoại theo mẫu 0XXX.XXX.XXX",
        regex: "^0\\d{3}\\.\\d{3}\\.\\d{3}$",
        errorMessage: "Số điện thoại không hợp lệ!",
        required: true,
      },
      {
        type: "date",
        label: "Ngày Đặt",
        name: "date",
        placeholder: "",
        regex: "",
        errorMessage: "Ngày đặt phải sau ngày hiện tại!",
        required: true,
        validateFunction: "checkOrderDate",
      },
      {
        type: "email",
        label: "Email Của Bạn",
        name: "email",
        placeholder: "Nhập email",
        regex: "@.*\\.com$",
        errorMessage: "Email không hợp lệ!",
        required: true,
      },
      {
        type: "file",
        label: "Ảnh Đại Diện",
        name: "avatar",
        accept: "image/*",
        errorMessage: "Vui lòng chọn ảnh đại diện!",
        required: true,
      },
    ],
    tableHeaders: [
      "STT",
      "Họ Và Tên",
      "Số Điện Thoại",
      "Ngày Đặt",
      "Email Của Bạn",
      "Ảnh Đại Diện",
    ],
  },

  // Template 3: Course Registration (based on ck/2)
  "course-registration": {
    title: "Đăng Kí Khóa Học",
    headerBgColor: "#ffffff",
    headerTextColor: "#000000",
    formBgColor: "#ffffff",
    formBorderColor: "#000000",
    footerBgColor: "#28a745", // success color
    footerTextColor: "#ffffff",
    footerText: "23630851_Lê Thành Long_DHCNTT19A",
    fields: [
      {
        type: "text",
        label: "Họ Và Tên",
        name: "name",
        placeholder: "Họ và Tên",
        regex: "^[A-Z][a-z]*(\\s+[A-Z][a-z]*)+$",
        errorMessage:
          "Mỗi từ phải bắt đầu bằng chữ hoa và phần còn lại viết thường",
        required: true,
        defaultValue: "Nguyen Van An",
      },
      {
        type: "tel",
        label: "Số Điện Thoại",
        name: "phone",
        placeholder: "Số điện thoại",
        regex: "^(0[9876543]\\d{2})\\.\\d{3}\\.\\d{3}$",
        errorMessage: "Số điện thoại phải theo mẫu: 0XXX.XXX.XXX",
        required: true,
      },
      {
        type: "email",
        label: "Email",
        name: "email",
        placeholder: "Email",
        regex: "^[a-zA-Z0-9_]{3,}@gmail\\.com$",
        errorMessage:
          "Email phải theo mẫu: name_email@gmail.com với name_email >= 3 ký tự!",
        required: true,
      },
      {
        type: "text",
        label: "Địa chỉ",
        name: "address",
        placeholder: "Địa chỉ",
        regex: "^[A-Za-z0-9\\/]+$",
        errorMessage: "Địa chỉ chỉ cho phép số, chữ và ký tự '/'!",
        required: true,
      },
      {
        type: "date",
        label: "Ngày sinh",
        name: "date",
        placeholder: "",
        regex: "",
        errorMessage: "Tuổi phải từ 12 trở lên!",
        required: true,
        validateFunction: "checkBirthDate",
      },
      {
        type: "radio",
        label: "Giáo viên",
        name: "gv",
        options: [
          { value: "Hà Nội", label: "Hà Nội" },
          { value: "TPHCM", label: "TPHCM" },
        ],
        required: true,
        errorMessage: "Vui lòng chọn giáo viên!",
      },
    ],
    tableHeaders: [
      "STT",
      "Họ Và Tên",
      "Số Điện Thoại",
      "Email",
      "Địa chỉ",
      "Năm sinh học viên",
      "Giáo viên",
    ],
  },
};

// Custom validation functions for templates
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

function checkOrderDate() {
  var date = $("#date").val();
  var today = new Date();
  var orderDate = new Date(date);

  if (!date) {
    return false;
  } else if (orderDate <= today) {
    return false;
  }
  return true;
}

function checkBirthDate() {
  var date = $("#date").val();
  if (!date) {
    return false;
  }

  let birthDate = new Date(date);
  let today = new Date();
  let age = today.getFullYear() - birthDate.getFullYear();
  let m = today.getMonth() - birthDate.getMonth();

  if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
    age--;
  }

  return age >= 12;
}
