$(document).ready(function () {
  let rowCount = 1;

  $("#registerBtn").on("click", function () {
    $("#generatedForm").submit();
  });

  function setupReadonlyFields() {
    const $source_select = $("#select");
    const $target_readonly_display = $("#readonly_display");

    function update_readonly_display() {
      const selectedValue = $source_select.val();
      if (selectedValue) {
        $target_readonly_display.val(selectedValue);
      } else {
        $target_readonly_display.val("");
      }
    }

    $source_select.on("change", update_readonly_display);
    update_readonly_display();
  }

  setupReadonlyFields();

  $("#generatedForm").on("submit", function (event) {
    event.preventDefault();

    let isValid = true;
    const text_inputInput = $("#text_input");
    const text_inputRegex = /^[A-Z][a-z]*(\s+[A-Z][a-z]*)+$/;
    const dateInput = $("#date");
    const phoneInput = $("#phone");
    const phoneRegex = /^(09|03|08)\d{8}$/;
    const emailInput = $("#email");
    const emailRegex = /.*@.*\.com$/;
    const selectInput = $("#select");

    $(".form-control").removeClass("is-invalid is-valid");
    $(".invalid-feedback").hide();

    if (text_inputInput.val().trim() === "") {
      text_inputInput.addClass("is-invalid");
      text_inputInput
        .siblings(".invalid-feedback")
        .text("Vui lòng nhập họ tên")
        .show();
      isValid = false;
    } else if (!text_inputRegex.test(text_inputInput.val().trim())) {
      text_inputInput.addClass("is-invalid");
      text_inputInput
        .siblings(".invalid-feedback")
        .text("sai định dạng ten")
        .show();
      isValid = false;
    } else {
      text_inputInput.addClass("is-valid");
    }

    if (dateInput.val() === "") {
      dateInput.addClass("is-invalid");
      dateInput
        .siblings(".invalid-feedback")
        .text("Vui lòng chọn ngày sinhh")
        .show();
      isValid = false;
    } else {
      const selectedDate = new Date(dateInput.val());
      const today = new Date();
      today.setHours(0, 0, 0, 0);
      let dateIsValid = true;
      let errorMessage = "";

      if (selectedDate >= today) {
        dateIsValid = false;
        errorMessage = "ngày sinh trc ngày hiên tại";
      }

      if (!dateIsValid) {
        dateInput.addClass("is-invalid");
        dateInput.siblings(".invalid-feedback").text(errorMessage).show();
        isValid = false;
      } else {
        dateInput.addClass("is-valid");
      }
    }

    if (phoneInput.val().trim() === "") {
      phoneInput.addClass("is-invalid");
      phoneInput
        .siblings(".invalid-feedback")
        .text("Vui lòng nhập số điện thoại")
        .show();
      isValid = false;
    } else if (!phoneRegex.test(phoneInput.val().trim())) {
      phoneInput.addClass("is-invalid");
      phoneInput.siblings(".invalid-feedback").text("sai định dạng dt").show();
      isValid = false;
    } else {
      phoneInput.addClass("is-valid");
    }

    if (emailInput.val().trim() === "") {
      emailInput.addClass("is-invalid");
      emailInput
        .siblings(".invalid-feedback")
        .text("Vui lòng nhập email")
        .show();
      isValid = false;
    } else if (!emailRegex.test(emailInput.val().trim())) {
      emailInput.addClass("is-invalid");
      emailInput
        .siblings(".invalid-feedback")
        .text("sai định dạng gmail")
        .show();
      isValid = false;
    } else {
      emailInput.addClass("is-valid");
    }

    if (selectInput.val() === "") {
      selectInput.addClass("is-invalid");
      selectInput
        .siblings(".invalid-feedback")
        .text("Vui lòng chọn chọn khóa học")
        .show();
      isValid = false;
    } else {
      selectInput.addClass("is-valid");
    }

    const radioRadio = $("input[name='radio']:checked");
    if (radioRadio.length === 0) {
      $("input[name='radio']").addClass("is-invalid");
      $("input[name='radio']")
        .first()
        .closest(".mb-3")
        .find(".invalid-feedback")
        .text("Vui lòng chọn một tùy chọn")
        .show();
      isValid = false;
    } else {
      $("input[name='radio']").addClass("is-valid");
    }

    const checkboxChecked = $("input[name='checkbox']:checked");
    if (checkboxChecked.length === 0) {
      $("input[name='checkbox']").addClass("is-invalid");
      $("input[name='checkbox']")
        .first()
        .closest(".mb-3")
        .find(".invalid-feedback")
        .text("Vui lòng chọn ít nhất một tùy chọn")
        .show();
      isValid = false;
    } else {
      $("input[name='checkbox']").addClass("is-valid");
    }

    if (isValid) {
      const rowData = {
        h__t_n: $("#text_input").val().trim() || "",
        ng_y_sinh: $("#date").val().trim() || "",
        sdt: $("#phone").val().trim() || "",
        Email_Address: $("#email").val().trim() || "",
        kh: $("#select").val().trim() || "",
        hth: $("input[name='radio']:checked").val() || "",
        k__n_ng_hc:
          $.map($("input[name='checkbox']:checked"), function (el) {
            return $(el).val();
          }).join(", ") || "",
      };

      addRowToTable(rowData);

      this.reset();
      $(".form-control").removeClass("is-valid is-invalid");

      $('img[id$="_preview"]').attr("src", "").hide();

      const modalElement = document.getElementById("myModal");
      if (modalElement) {
        const modalInstance = bootstrap.Modal.getInstance(modalElement);
        if (modalInstance) {
          modalInstance.hide();
        } else {
          $("#myModal").modal("hide");
        }
      }
    }
  });

  function addRowToTable(rowData) {
    const $tableBody = $("#dataTableBody");
    const $newRow = $("<tr></tr>");

    $newRow.append($("<td></td>").text(rowCount++));

    $newRow.append($("<td></td>").text(rowData.h__t_n || ""));
    $newRow.append($("<td></td>").text(rowData.ng_y_sinh || ""));
    $newRow.append($("<td></td>").text(rowData.sdt || ""));
    $newRow.append($("<td></td>").text(rowData.Email_Address || ""));
    $newRow.append($("<td></td>").text(rowData.kh || ""));
    $newRow.append($("<td></td>").text(rowData.hth || ""));
    $newRow.append($("<td></td>").text(rowData.k__n_ng_hc || ""));

    $tableBody.append($newRow);
  }

  $("#date").on("change", function () {
    const selectedDate = new Date($(this).val());
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    let isValid = true;
    let errorMessage = "";

    if (selectedDate >= today) {
      isValid = false;
      errorMessage = "ngày sinh trc ngày hiên tại";
    }

    if (!isValid) {
      $(this).addClass("is-invalid").removeClass("is-valid");
      $(this).siblings(".invalid-feedback").text(errorMessage).show();
    } else {
      $(this).removeClass("is-invalid").addClass("is-valid");
    }
  });
});
