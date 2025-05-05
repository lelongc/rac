// Combined jQuery script for form validation and table updating
$(document).ready(function() {
  // Set up listeners for readonly fields
  let rowCount = 1;
  function setupReadonlyFields() {
    const $source_select = $("#select");
    const $target_readonly_display = $("#readonly_display");

    function update_readonly_display() {
      const selectedValue = $source_select.val();
      // Update only if a valid option (not the default 'Choose...') is selected
      if (selectedValue) {
          $target_readonly_display.val(selectedValue);
      } else {
          $target_readonly_display.val(""); // Clear if default is selected
      }
    }

    // Update on change
    $source_select.on("change", update_readonly_display);

    // Initial update on load
    update_readonly_display();

  }

  // Initialize readonly fields
  setupReadonlyFields();

  // Form validation and submission handler
  $("#generatedForm").on("submit", function(event) {
    // *** PREVENT DEFAULT SUBMISSION FIRST ***
    event.preventDefault();

    // --- Your validation logic here ---
    let isValid = true; // Assume valid initially
    const text_inputInput = $("#text_input");
    const text_inputPattern = /^[A-Z][a-z]*(\s+[A-Z][a-z]*)+$/; // Pattern from HTML
    const phoneInput = $("#phone");
    const phonePattern = /^(09|03|08)\d{8}$/; // Pattern from HTML
    const emailInput = $("#email");
    const emailPattern = /@.*\.com$/; // Pattern from HTML

    // Reset previous validation states
    $(".form-control").removeClass("is-invalid is-valid");
    $(".invalid-feedback").hide(); // Hide feedback initially

    // Validate ho ten (text_input)
    if (text_inputInput.val().trim() !== "") {
      if (!text_inputPattern.test(text_inputInput.val().trim())) {
      text_inputInput.addClass("is-invalid");
      text_inputInput.siblings(".invalid-feedback").text("hts").show();
      isValid = false;
    } else {
      text_inputInput.addClass("is-valid");
    }
    }

    // Validate Phone Number (phone)
    if (phoneInput.val().trim() !== "") {
      if (!phonePattern.test(phoneInput.val().trim())) {
      phoneInput.addClass("is-invalid");
      phoneInput.siblings(".invalid-feedback").text("ps").show();
      isValid = false;
    } else {
      phoneInput.addClass("is-valid");
    }
    }

    // Validate Email Address (email)
    if (emailInput.val().trim() !== "") {
      if (!emailPattern.test(emailInput.val().trim())) {
      emailInput.addClass("is-invalid");
      emailInput.siblings(".invalid-feedback").text("ms").show();
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
        na: $("#text_input").val().trim() || "",
        nga: $("#date").val().trim() || "",
        pho: $("#phone").val().trim() || "",
        ma: $("#email").val().trim() || "",
        kh: $("#select").val().trim() || "",
        hth: $("input[name='radio']:checked").val() || "",
        kn: $.map($("input[name='checkbox']:checked"), function(el) { return $(el).val(); }).join(", ") || ""
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
    $newRow.append($("<td></td>").text(rowData.na || "")); // Corresponds to 'na' header
    $newRow.append($("<td></td>").text(rowData.nga || "")); // Corresponds to 'nga' header
    $newRow.append($("<td></td>").text(rowData.pho || "")); // Corresponds to 'pho' header
    $newRow.append($("<td></td>").text(rowData.ma || "")); // Corresponds to 'ma' header
    $newRow.append($("<td></td>").text(rowData.kh || "")); // Corresponds to 'kh' header
    $newRow.append($("<td></td>").text(rowData.hth || "")); // Corresponds to 'hth' header
    $newRow.append($("<td></td>").text(rowData.kn || "")); // Corresponds to 'kn' header
    $tableBody.append($newRow);
    rowCount++;
  }
}); // End of $(document).ready