// Combined jQuery script for form validation and table updating
$(document).ready(function () {
  // Form validation and submission handler
  let rowCount = 1;
  $("#generatedForm").on("submit", function (event) {
    // *** PREVENT DEFAULT SUBMISSION FIRST ***
    event.preventDefault();

    // --- Your validation logic here ---
    let isValid = true; // Assume valid initially
    const emailInput = $("#email");
    const dateInput = $("#date"); // Add missing variable declaration
    const emailPattern = /@.*\.com$/; // Pattern from HTML

    // Reset previous validation states
    $(".form-control").removeClass("is-invalid is-valid");
    $(".invalid-feedback").hide(); // Hide feedback initially

    // Validate Date (date)
    if (dateInput.val() !== "") {
      const selectedDate = new Date(dateInput.val());
      const today = new Date();
      today.setHours(0, 0, 0, 0);
      const minYearsDate = new Date(today);
      minYearsDate.setFullYear(today.getFullYear() - 12);
      if (selectedDate > minYearsDate) {
        dateInput.addClass("is-invalid");
        dateInput
          .siblings(".invalid-feedback")
          .text("Ngày phải sau 12 năm trước")
          .show();
        isValid = false;
      } else if (
        selectedDate >
        new Date(today.getFullYear() - 12, today.getMonth(), today.getDate())
      ) {
        dateInput.addClass("is-invalid");
        dateInput
          .siblings(".invalid-feedback")
          .text("Ngày không được sau 12 năm trước")
          .show();
        isValid = false;
      } else {
        dateInput.addClass("is-valid");
      }
    }

    // Validate Email Address (email)
    if (emailInput.val().trim() !== "") {
      if (!emailPattern.test(emailInput.val().trim())) {
        emailInput.addClass("is-invalid");
        emailInput
          .siblings(".invalid-feedback")
          .text("aaaaaaaaaaaaaaaaa")
          .show();
        isValid = false;
      } else {
        emailInput.addClass("is-valid");
      }
    }

    // --- End of validation logic ---

    // Only proceed if the form is valid
    if (isValid) {
      // Collect form data
      const rowData = {
        date: $("#date").val().trim() || "",
        email: $("#email").val().trim() || "",
      };

      // Add data to table
      addRowToTable(rowData);

      // Reset form
      this.reset();
      $(".form-control").removeClass("is-valid is-invalid"); // Clear validation classes on reset

      // Hide modal (using Bootstrap 5 instance if available)
      const modalElement = document.getElementById("myModal");
      if (modalElement) {
        const modalInstance = bootstrap.Modal.getInstance(modalElement);
        if (modalInstance) {
          modalInstance.hide();
        } else {
          // Fallback for older Bootstrap or if instance isn't found
          $("#myModal").modal("hide");
        }
      }
    }
    // If !isValid, the invalid feedback is already shown by the validation logic
  });

  // Function to add a new row to the table
  function addRowToTable(rowData) {
    const $tableBody = $("#dataTableBody"); // Target the table in your HTML
    const $newRow = $("<tr></tr>");
    $newRow.append($("<td></td>").text(rowCount));
    $newRow.append($("<td></td>").text(rowData.date || "")); // Fixed property access
    $newRow.append($("<td></td>").text(rowData.email || "")); // Fixed property access
    $tableBody.append($newRow);
    rowCount++;
  }
}); // End of $(document).ready
