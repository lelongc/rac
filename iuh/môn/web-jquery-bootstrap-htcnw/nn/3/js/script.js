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
    const phoneRegex = /^0\d{3}\.\d{3}\.\d{3}$/;
    const dateInput = $("#date");
    const emailInput = $("#email");
    const emailRegex = /^[a-zA-Z0-9_]{3,}@gmail\.com$/;
    const image_uploadInput = $("#image_upload");

    $(".form-control").removeClass("is-invalid is-valid");
    $(".invalid-feedback").hide();

    if (text_inputInput.val().trim() === "") {
      text_inputInput.addClass("is-invalid");
      text_inputInput
        .siblings(".invalid-feedback")
        .text("Vui lòng nhập họ và tên")
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

    if (phoneInput.val().trim() === "") {
      phoneInput.addClass("is-invalid");
      phoneInput
        .siblings(".invalid-feedback")
        .text("Vui lòng nhập số  điện thoại")
        .show();
      isValid = false;
    } else if (!phoneRegex.test(phoneInput.val().trim())) {
      phoneInput.addClass("is-invalid");
      phoneInput.siblings(".invalid-feedback").text("sai định dangsdt").show();
      isValid = false;
    } else {
      phoneInput.addClass("is-valid");
    }

    if (dateInput.val() !== "") {
      {
        const selectedDate = new Date(dateInput.val());
        const today = new Date();
        today.setHours(0, 0, 0, 0);
        let dateIsValid = true;
        let errorMessage = "";

        if (selectedDate < today) {
          dateIsValid = false;
          errorMessage = "sau ngày hiện tịa";
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

    if (emailInput.val().trim() === "") {
      emailInput.addClass("is-invalid");
      emailInput
        .siblings(".invalid-feedback")
        .text("Vui lòng nhập mail")
        .show();
      isValid = false;
    } else if (!emailRegex.test(emailInput.val().trim())) {
      emailInput.addClass("is-invalid");
      emailInput.siblings(".invalid-feedback").text("sai định dạng mau").show();
      isValid = false;
    } else {
      emailInput.addClass("is-valid");
    }

    if (image_uploadInput.get(0).files.length === 0) {
      image_uploadInput.addClass("is-invalid");
      image_uploadInput
        .siblings(".invalid-feedback")
        .text("Vui lòng chọn upload image")
        .show();
      isValid = false;
    } else {
      image_uploadInput.addClass("is-valid");
    }

    if (isValid) {
      const rowData = {
        h: $("#text_input").val().trim() || "",
        s: $("#phone").val().trim() || "",
        n: $("#date").val().trim() || "",
        km: $("#email").val().trim() || "",
        a: $("#image_upload_preview").attr("src") || "",
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

    $newRow.append($("<td></td>").text(rowData.h || ""));
    $newRow.append($("<td></td>").text(rowData.s || ""));
    $newRow.append($("<td></td>").text(rowData.n || ""));
    $newRow.append($("<td></td>").text(rowData.km || ""));
    if (rowData.a) {
      const $cell = $("<td></td>");
      $("<img>")
        .attr({
          src: rowData.a,
          style: "max-width:100px; max-height:100px;",
        })
        .appendTo($cell);
      $newRow.append($cell);
    } else {
      $newRow.append($("<td></td>"));
    }

    $tableBody.append($newRow);
  }

  $("#date").on("change", function () {
    const selectedDate = new Date($(this).val());
    const today = new Date();
    today.setHours(0, 0, 0, 0);
    let isValid = true;
    let errorMessage = "";

    if (selectedDate < today) {
      isValid = false;
      errorMessage = "sau ngày hiện tịa";
    }

    if (!isValid) {
      $(this).addClass("is-invalid").removeClass("is-valid");
      $(this).siblings(".invalid-feedback").text(errorMessage).show();
    } else {
      $(this).removeClass("is-invalid").addClass("is-valid");
    }
  });
});
