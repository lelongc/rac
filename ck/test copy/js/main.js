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

    $(".form-control").removeClass("is-invalid is-valid");
    $(".invalid-feedback").hide();

    if (isValid) {
      const rowData = {
        _: $("#select").val().trim() || "",
        ma: $("#date").val().trim() || "",
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

    $newRow.append($("<td></td>").text(rowData._ || ""));
    $newRow.append($("<td></td>").text(rowData.ma || ""));

    $tableBody.append($newRow);
  }
});
