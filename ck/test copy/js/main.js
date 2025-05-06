$(document).ready(function () {
  let rowCount = 1;

  function setupReadonlyFields() {
    const $source_select = $("#select");
    const $target_readonly_display = $("#readonly_display");

    function update_readonly_display() {
      const selectedValue = $source_select.val();
      if (selectedValue) {
        const selectedText = $source_select.find("option:selected").text();
        $target_readonly_display.val(selectedText);
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
    const text_inputPattern = /^[A-Z][a-z]*(\s+[A-Z][a-z]*)+$/;
    const dateInput = $("#date");
    const phoneInput = $("#phone");
    const phonePattern = /^(01|03|08)\d{8}$/;
    const emailInput = $("#email");
    const emailPattern = /@.*gmail.*\.com$/;

    $(".form-control").removeClass("is-invalid is-valid");
    $(".invalid-feedback").hide();

    if (text_inputInput.val().trim() !== "") {
      if (!text_inputPattern.test(text_inputInput.val().trim())) {
        text_inputInput.addClass("is-invalid");
        text_inputInput
          .siblings(".invalid-feedback")
          .text("sai định dạng")
          .show();
        isValid = false;
      } else {
        text_inputInput.addClass("is-valid");
      }
    }

    if (dateInput.val() !== "") {
      {
        const selectedDate = new Date(dateInput.val());
        const today = new Date();
        today.setHours(0, 0, 0, 0);
        let dateIsValid = true;
        let errorMessage = "";

        if (selectedDate >= today) {
          dateIsValid = false;
          errorMessage = "phải trước hôm na";
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

    if (phoneInput.val().trim() !== "") {
      if (!phonePattern.test(phoneInput.val().trim())) {
        phoneInput.addClass("is-invalid");
        phoneInput.siblings(".invalid-feedback").text("sai định dạng").show();
        isValid = false;
      } else {
        phoneInput.addClass("is-valid");
      }
    }

    if (emailInput.val().trim() !== "") {
      if (!emailPattern.test(emailInput.val().trim())) {
        emailInput.addClass("is-invalid");
        emailInput.siblings(".invalid-feedback").text("sai định dạng").show();
        isValid = false;
      } else {
        emailInput.addClass("is-valid");
      }
    }

    if (isValid) {
      const rowData = {
        h__v__t_n: $("#text_input").val().trim() || "",
        ng_y_sinh: $("#date").val().trim() || "",
        _i_n_tho_i: $("#phone").val().trim() || "",
        gmail: $("#email").val().trim() || "",
        kh_a_h_c: $("#select").val().trim() || "",
        h_nh_th_c_h_c: $("input[name='radio']:checked").val() || "",
        k__n_ng_hc:
          $.map($("input[name='checkbox']:checked"), function (el) {
            return $(el).val();
          }).join(", ") || "",
      };

      addRowToTable(rowData);

      this.reset();
      $(".form-control").removeClass("is-valid is-invalid");

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

    $newRow.append($("<td></td>").text(rowData.h__v__t_n || ""));
    $newRow.append($("<td></td>").text(rowData.ng_y_sinh || ""));
    $newRow.append($("<td></td>").text(rowData._i_n_tho_i || ""));
    $newRow.append($("<td></td>").text(rowData.gmail || ""));
    $newRow.append($("<td></td>").text(rowData.kh_a_h_c || ""));
    $newRow.append($("<td></td>").text(rowData.h_nh_th_c_h_c || ""));
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
      errorMessage = "phải trước hôm na";
    }

    if (!isValid) {
      $(this).addClass("is-invalid").removeClass("is-valid");
      $(this).siblings(".invalid-feedback").text(errorMessage).show();
    } else {
      $(this).removeClass("is-invalid").addClass("is-valid");
    }
  });
});
