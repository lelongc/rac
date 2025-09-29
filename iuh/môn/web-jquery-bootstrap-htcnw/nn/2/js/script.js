$(document).ready(function () {
  let rowCount = 1;

  $("#registerBtn").on("click", function () {
    $("#generatedForm").submit();
  });

  function setupImagePreviews() {
    $('input[type="file"][accept="image/*"]').each(function () {
      const inputId = $(this).attr("id");
      const previewId = inputId + "_preview";

      $(this).on("change", function () {
        const file = this.files[0];
        if (file) {
          const reader = new FileReader();
          reader.onload = function (e) {
            $("#" + previewId)
              .attr("src", e.target.result)
              .hide();
          };
          reader.readAsDataURL(file);
        } else {
          $("#" + previewId)
            .attr("src", "")
            .hide();
        }
      });
    });
  }

  setupImagePreviews();

  function setupReadonlyFields() {}

  setupReadonlyFields();

  $("#generatedForm").on("submit", function (event) {
    event.preventDefault();

    let isValid = true;
    const text_inputInput = $("#text_input");
    const text_inputRegex = /^[A-Z][a-z]*(\s+[A-Z][a-z]*)+$/;
    const phoneInput = $("#phone");
    const phoneRegex = /^0[3-9]\d{2}\.\d{3}\.\d{3}$/;
    const emailInput = $("#email");
    const emailRegex = /^[a-zA-Z0-9_]{3,}@gmail\.com$/;
    const addressInput = $("#address");
    const addressRegex = /^[a-zA-Z0-9/]+$/;
    const dateInput = $("#date");

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
        .text("nhập sai định dạng họ tên")
        .show();
      isValid = false;
    } else {
      text_inputInput.addClass("is-valid");
    }

    if (phoneInput.val().trim() === "") {
      phoneInput.addClass("is-invalid");
      phoneInput
        .siblings(".invalid-feedback")
        .text("Vui lòng nhập phone")
        .show();
      isValid = false;
    } else if (!phoneRegex.test(phoneInput.val().trim())) {
      phoneInput.addClass("is-invalid");
      phoneInput.siblings(".invalid-feedback").text("sai định dạng sdt").show();
      isValid = false;
    } else {
      phoneInput.addClass("is-valid");
    }

    if (emailInput.val().trim() === "") {
      emailInput.addClass("is-invalid");
      emailInput
        .siblings(".invalid-feedback")
        .text("Vui lòng nhập email address")
        .show();
      isValid = false;
    } else if (!emailRegex.test(emailInput.val().trim())) {
      emailInput.addClass("is-invalid");
      emailInput
        .siblings(".invalid-feedback")
        .text("sai định dạng email")
        .show();
      isValid = false;
    } else {
      emailInput.addClass("is-valid");
    }

    if (addressInput.val().trim() === "") {
      addressInput.addClass("is-invalid");
      addressInput
        .siblings(".invalid-feedback")
        .text("Vui lòng nhập địa chỉ")
        .show();
      isValid = false;
    } else if (!addressRegex.test(addressInput.val().trim())) {
      addressInput.addClass("is-invalid");
      addressInput
        .siblings(".invalid-feedback")
        .text("sai định dạng địa chủ")
        .show();
      isValid = false;
    } else {
      addressInput.addClass("is-valid");
    }

    if (dateInput.val() !== "") {
      {
        const selectedDate = new Date(dateInput.val());
        const today = new Date();
        today.setHours(0, 0, 0, 0);
        let dateIsValid = true;
        let errorMessage = "";

        const limitDate = new Date(today);
        limitDate.setFullYear(today.getFullYear() - 12);
        if (selectedDate > limitDate) {
          dateIsValid = false;
          errorMessage = "phải trên 12";
        }

        if (!dateIsValid) {
          dateInput.addClass("is-invalid");
          dateInput.siblings(".invalid-feedback").text(errorMessage).show();
          isValid = false;
        } else {
          dateInput.addClass("is-valid");
        }
      }
    }

    const radioRadio = $("input[name='radio']:checked");
    if (radioRadio.length === 0) {
      $("input[name='radio']").addClass("is-invalid");
      $("input[name='radio']")
        .siblings(".invalid-feedback")
        .text("Vui lòng chọn một tùy chọn")
        .show();
      isValid = false;
    } else {
      $("input[name='radio']").addClass("is-valid");
    }

    if (isValid) {
      const rowData = {
        h__t_n: $("#text_input").val().trim() || "",
        so_dien_tho_i: $("#phone").val().trim() || "",
        email: $("#email").val().trim() || "",
        __a_ch_: $("#text_input").val().trim() || "",
        n_m_sinh_sinh_vi_n: $("#date").val().trim() || "",
        gi_o_vi_n: $("input[name='radio']:checked").val() || "",
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
    $newRow.append($("<td></td>").text(rowData.so_dien_tho_i || ""));
    $newRow.append($("<td></td>").text(rowData.email || ""));
    $newRow.append($("<td></td>").text(rowData.__a_ch_ || ""));
    $newRow.append($("<td></td>").text(rowData.n_m_sinh_sinh_vi_n || ""));
    $newRow.append($("<td></td>").text(rowData.gi_o_vi_n || ""));

    $tableBody.append($newRow);
  }

  $("#date").on("change", function () {
    const selectedDate = new Date($(this).val());
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    let isValid = true;
    let errorMessage = "";

    const limitDate = new Date(today);
    limitDate.setFullYear(today.getFullYear() - 12);
    if (selectedDate > limitDate) {
      isValid = false;
      errorMessage = "phải trên 12";
    }

    if (!isValid) {
      $(this).addClass("is-invalid").removeClass("is-valid");
      $(this).siblings(".invalid-feedback").text(errorMessage).show();
    } else {
      $(this).removeClass("is-invalid").addClass("is-valid");
    }
  });
});
