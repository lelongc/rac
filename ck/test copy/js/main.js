$(document).ready(function () {
  let rowCount = 1;

  // Setup image preview functionality
  function setupImagePreviews() {
    $('input[type="file"][accept="image/*"]').each(function () {
      const inputId = $(this).attr("id");
      const previewId = inputId + "_preview";

      $(this).on("change", function () {
        const file = this.files[0];
        if (file) {
          const reader = new FileReader();
          reader.onload = function (e) {
            // Store the image data but don't display it
            $("#" + previewId)
              .attr("src", e.target.result)
              .hide(); // Keep hiding the preview
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

    $(".form-control").removeClass("is-invalid is-valid");
    $(".invalid-feedback").hide();

    if (isValid) {
      const rowData = {
        ma: $("#select").val().trim() || "",
        mail: $("#image_upload_preview").attr("src") || "",
      };

      addRowToTable(rowData);

      this.reset();
      $(".form-control").removeClass("is-valid is-invalid");
      // Reset image previews
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

    $newRow.append($("<td></td>").text(rowData.ma || ""));
    if (rowData.mail) {
      const $cell = $("<td></td>");
      $("<img>")
        .attr({
          src: rowData.mail,
          style: "max-width:100px; max-height:100px;",
        })
        .appendTo($cell);
      $newRow.append($cell);
    } else {
      $newRow.append($("<td></td>"));
    }

    $tableBody.append($newRow);
  }
});
