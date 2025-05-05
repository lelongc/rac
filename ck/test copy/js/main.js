// Combined jQuery script for form validation and table updating
$(document).ready(function () {
  // Form validation and submission handler
  $("#generatedForm").on("submit", function (event) {
    // *** PREVENT DEFAULT SUBMISSION FIRST ***
    event.preventDefault();

    // --- Your validation logic here ---
    let isValid = true; // Assume valid initially
    const phoneInput = $("#phone");
    const phonePattern = /^[A-Z][a-z]*(\s+[A-Z][a-z]*)+$/; // Pattern from HTML
    const text_inputInput = $("#text_input");
    const text_inputPattern = /@.*\.com$/; // Pattern from HTML

    // Reset previous validation states
    $(".form-control").removeClass("is-invalid is-valid");
    $(".invalid-feedback").hide(); // Hide feedback initially

    // Validate Phone Number (phone)
    if (phoneInput.val().trim() !== "") {
      if (!phonePattern.test(phoneInput.val().trim())) {
        phoneInput.addClass("is-invalid");
        phoneInput.siblings(".invalid-feedback").text("ffffffffffff").show();
        isValid = false;
      } else {
        phoneInput.addClass("is-valid");
      }
    }

    // Validate Text Input (text_input)
    if (text_inputInput.val().trim() !== "") {
      if (!text_inputPattern.test(text_inputInput.val().trim())) {
        text_inputInput.addClass("is-invalid");
        text_inputInput
          .siblings(".invalid-feedback")
          .text("aaaaaaaaaaaaaaaaa")
          .show();
        isValid = false;
      } else {
        text_inputInput.addClass("is-valid");
      }
    }

    // --- End of validation logic ---

    // Only proceed if the form is valid
    if (isValid) {
      // Collect form data
      const rowData = {
        ten: $("#phone").val().trim() || "",
        ma: $("#text_input").val().trim() || "",
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
    const rowCount = $tableBody.children().length + 1;
    $newRow.append($("<td></td>").text(rowCount));
    // $newRow.append($("<td></td>").text(rowCount));
    $newRow.append($("<td></td>").text(rowData.ten || "")); // Corresponds to 'ten' header
    $newRow.append($("<td></td>").text(rowData.ma || "")); // Corresponds to 'ma' header
    $tableBody.append($newRow);
  }
}); // End of $(document).ready
