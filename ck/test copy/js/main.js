$(document).ready(function () {
  let rowCount = 1;

  // Setup image preview functionality
  function setupImagePreviews() {
    $('input[type="file"][accept="image/*"]').each(function() {
      const inputId = $(this).attr('id');
      const previewId = inputId + '_preview';
      
      $(this).on('change', function() {
        const file = this.files[0];
        if (file) {
          const reader = new FileReader();
          reader.onload = function(e) {
            $('#' + previewId).attr('src', e.target.result).show();
          }
          reader.readAsDataURL(file);
        } else {
          $('#' + previewId).attr('src', '').hide();
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
       $target_readonly_display.val($source_select.find("option:selected").text());
      } else {
          $target_readonly_display.val("");
      }
    }
    
    $source_select.on("change", update_readonly_display);
    update_readonly_display();
  }

  setupReadonlyFields();

  $("#generatedForm").on("submit", function(event) {
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
      const today = new Date(); today.setHours(0,0,0,0);
      let dateIsValid = true;
      let errorMessage = "";
      
      if (selectedDate >= today) {
        dateIsValid = false;
        errorMessage = "ỷyery";
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
      text_inputInput.siblings(".invalid-feedback").text("hghhfghfh").show();
      isValid = false;
    } else {
      text_inputInput.addClass("is-valid");
    }
    }

    if (isValid) {
      const rowData = {
        h: $("#image_upload_preview").attr("src") || "",
        hh: $("#select").val().trim() || "",
        jj: $("#date").val().trim() || "",
        jgjgj: $("#text_input").val().trim() || ""
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
  
  if (rowData.h) {
    const $cell = $("<td></td>");
    $("<img>").attr({
      src: rowData.h,
      style: "max-width:100px; max-height:100px;"
    }).appendTo($cell);
    $newRow.append($cell);
  } else {
    $newRow.append($("<td></td>"));
  }
    $newRow.append($("<td></td>").text(rowData.hh || ""));
    $newRow.append($("<td></td>").text(rowData.jj || ""));
    $newRow.append($("<td></td>").text(rowData.jgjgj || ""));
  
  $tableBody.append($newRow);
}

  $('#date').on('change', function() {
    const selectedDate = new Date($(this).val());
    const today = new Date(); today.setHours(0,0,0,0);
    let isValid = true;
    let errorMessage = "";
    
    if (selectedDate >= today) {
      isValid = false;
      errorMessage = "ỷyery";
    }
    
    if (!isValid) {
      $(this).addClass('is-invalid').removeClass('is-valid');
      $(this).siblings('.invalid-feedback').text(errorMessage).show();
    } else {
      $(this).removeClass('is-invalid').addClass('is-valid');
    }
  });
});