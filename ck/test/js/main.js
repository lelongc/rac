/**
 * Validate the name field
 * Requirements: Not empty, each word must start with uppercase (e.g., Le Van An)
 */

/**
 * Format date from yyyy-mm-dd to dd/mm/yyyy
 */
function formatDate(dateString) {
  if (!dateString) return "";
  const date = new Date(dateString);
  const day = date.getDate().toString().padStart(2, "0");
  const month = (date.getMonth() + 1).toString().padStart(2, "0");
  const year = date.getFullYear();
  return `${day}/${month}/${year}`;
}

/**
 * Register a new course enrollment
 * Validates all fields before proceeding
 */
function DangKy() {
  var nameValid = true;
  var dobValid = true;
  var phoneValid = true;
  var emailValid = true;
  var methodValid = true;
  var skillsValid = true;

  // Only proceed if all validations pass
  if (
    !nameValid ||
    !dobValid ||
    !phoneValid ||
    !emailValid ||
    !methodValid ||
    !skillsValid
  ) {
    return; // Stop if any validation fails
  }

  // Gather form data

  // Add new row to the table
  var rowCount = $("#memberList tbody tr").length + 1;
  var newRow = `<tr>
                    <td>${rowCount}</td>
                  </tr>`;
  $("#memberList tbody").append(newRow);

  // Hide the modal
  $("#myModal").modal("hide");

  // Reset form
}

// Initialize when the document is ready
$(document).ready(function () {});
