$(document).ready(function () {
  let rowCount = 1;

  // Add click event for register button
  $("#registerBtn").on("click", function () {
    $("#generatedForm").submit();
  });

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
            $("#" + previewId)
              .attr("src", e.target.result)
              .show();
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
    const text_inputInput = $("#text_input");
    const text_inputPattern = /^[A-Z][a-z]*(\s+[A-Z][a-z]*)+$/;
    const dateInput = $("#date");

    $(".form-control").removeClass("is-invalid is-valid");
    $(".invalid-feedback").hide();

    if (text_inputInput.val().trim() === "") {
      text_inputInput.addClass("is-invalid");
      text_inputInput
        .siblings(".invalid-feedback")
        .text("Vui lòng nhập text input")
        .show();
      isValid = false;
    } else if (!text_inputPattern.test(text_inputInput.val().trim())) {
      text_inputInput.addClass("is-invalid");
      text_inputInput.siblings(".invalid-feedback").text("ss").show();
      isValid = false;
    } else {
      text_inputInput.addClass("is-valid");
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
          errorMessage = "aaaa";
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

    if (isValid) {
      const rowData = {
        name: $("#text_input").val().trim() || "",
        date: $("#date").val().trim() || "",
        pho: $("#phone").val().trim() || "",
        sec: $("#select").val().trim() || "",
        rad: $("input[name='radio']:checked").val() || "",
        imh: $("#image_upload_preview").attr("src") || "",
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

    $newRow.append($("<td></td>").text(rowData.name || ""));
    $newRow.append($("<td></td>").text(rowData.date || ""));
    $newRow.append($("<td></td>").text(rowData.pho || ""));
    $newRow.append($("<td></td>").text(rowData.sec || ""));
    $newRow.append($("<td></td>").text(rowData.rad || ""));
    if (rowData.imh) {
      const $cell = $("<td></td>");
      $("<img>")
        .attr({
          src: rowData.imh,
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

    if (selectedDate >= today) {
      isValid = false;
      errorMessage = "aaaa";
    }

    if (!isValid) {
      $(this).addClass("is-invalid").removeClass("is-valid");
      $(this).siblings(".invalid-feedback").text(errorMessage).show();
    } else {
      $(this).removeClass("is-invalid").addClass("is-valid");
    }
  });
});
