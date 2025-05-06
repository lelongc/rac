$(document).ready(function () {
  let rowCount = 1;

  function setupReadonlyFields() {}

  setupReadonlyFields();

  $("#generatedForm").on("submit", function (event) {
    event.preventDefault();

    let isValid = true;
    const dateInput = $("#date");
    const text_inputInput = $("#text_input");
    const text_inputPattern = /^[A-Z][a-z]*(\s+[A-Z][a-z]*)+$/;

    $(".form-control").removeClass("is-invalid is-valid");
    $(".invalid-feedback").hide();

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
          errorMessage = "123";
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

    if (text_inputInput.val().trim() !== "") {
      if (!text_inputPattern.test(text_inputInput.val().trim())) {
        text_inputInput.addClass("is-invalid");
        text_inputInput.siblings(".invalid-feedback").text("ten sai").show();
        isValid = false;
      } else {
        text_inputInput.addClass("is-valid");
      }
    }

    if (isValid) {
      const rowData = {
        ten: $("#text_input").val().trim() || "",
        tuoi: $("#date").val().trim() || "",
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

    $newRow.append($("<td></td>").text(rowData.ten || ""));
    $newRow.append($("<td></td>").text(rowData.tuoi || ""));

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
      errorMessage = "123";
    }

    if (!isValid) {
      $(this).addClass("is-invalid").removeClass("is-valid");
      $(this).siblings(".invalid-feedback").text(errorMessage).show();
    } else {
      $(this).removeClass("is-invalid").addClass("is-valid");
    }
  });
});
