# GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE TRONG BỘ XỬ LÝ LỖI TOÀN CỤC (GLOBAL EXCEPTION HANDLER)

> **Mục tiêu**: Nắm vững cơ chế xử lý lỗi tập trung (Centralized Exception Handling) bằng `@ControllerAdvice` và `@ExceptionHandler`. Hiểu tại sao ứng dụng không bao giờ bị văng màn hình trắng 500 HTML mà luôn trả về định dạng JSON chuyên nghiệp cho Frontend.

---

## 1. MÃ NGUỒN ĐẦY ĐỦ CỦA 3 FILE TRONG PACKAGE EXCEPTION

### 1.1. `AppException.java` (`src/main/java/com/group/blog/exception/AppException.java`)
```java
package com.group.blog.exception;

public class AppException extends RuntimeException {
    private ErrorCode errorCode;

    public AppException(ErrorCode errorCode) {
        super(errorCode.getMessage());
        this.errorCode = errorCode;
    }

    public ErrorCode getErrorCode() {
        return errorCode;
    }

    public void setErrorCode(ErrorCode errorCode) {
        this.errorCode = errorCode;
    }
}
```

### 1.2. `ErrorCode.java` (`src/main/java/com/group/blog/exception/ErrorCode.java`)
```java
package com.group.blog.exception;

public enum ErrorCode {
    UNCATEGORIZED_EXCEPTION(9999, "Uncategorized error"),
    INVALID_KEY(1001, "Invalid message key"),
    USER_EXITED(1002, "User Exited"),
    USERNAME_INVALID(1003, "Username must be at least 3 charactes"),
    INVALID_PASSWORD(1004, "Password must be at least 8 characters"),
    USER_NOT_EXITED(1005, "User Not Exited"),
    UNAUTHENTICATED(1006, "Unauthenticated"),
    PASSWORD_INCORRECT(1007, "Mật khẩu cũ không chính xác"),
    PASSWORD_NOT_MATCH(1008, "Mật khẩu xác nhận không khớp"),
    CATEGORY_NOT_FOUND(1009, "Danh mục không tồn tại"),
    BLOG_NOT_FOUND(1010, "Bài viết không tồn tại"),
    UNAUTHORIZED(1011, "Bạn không có quyền thực hiện hành động này"),
    CATEGORY_EXITED(1012, "Danh mục đã tồn tại"),
    ;

    private int code;
    private String message;

    ErrorCode(int code, String message){
        this.message = message;
        this.code = code;
    }

    public int getCode() {
        return code;
    }

    public String getMessage() {
        return message;
    }
}
```

### 1.3. `GlobalExceptionHandler.java` (`src/main/java/com/group/blog/exception/GlobalExceptionHandler.java`)
```java
package com.group.blog.exception;

import com.group.blog.dto.request.ApiResponse;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

@ControllerAdvice
public class GlobalExceptionHandler {

    // 1. Bắt tất cả các lỗi không xác định (Lỗi hệ thống bất ngờ)
    @ExceptionHandler(value = Exception.class)
    ResponseEntity<ApiResponse> handlingException(Exception exception){
        ApiResponse apiResponse = new ApiResponse();
        apiResponse.setCode(ErrorCode.UNCATEGORIZED_EXCEPTION.getCode());
        apiResponse.setMessage(ErrorCode.UNCATEGORIZED_EXCEPTION.getMessage());
        return ResponseEntity.badRequest().body(apiResponse);
    }

    // 2. Bắt các ngoại lệ nghiệp vụ tùy biến (AppException)
    @ExceptionHandler(value = AppException.class)
    ResponseEntity<ApiResponse> handlingAppException(AppException exception){
        ErrorCode errorCode = exception.getErrorCode();
        ApiResponse apiResponse = new ApiResponse();
        apiResponse.setCode(errorCode.getCode());
        apiResponse.setMessage(errorCode.getMessage());
        return ResponseEntity.badRequest().body(apiResponse);
    }

    // 3. Bắt các lỗi vi phạm dữ liệu đầu vào (@Valid DTO)
    @ExceptionHandler(value = MethodArgumentNotValidException.class)
    ResponseEntity<ApiResponse> handlingValidation(MethodArgumentNotValidException except){
        String enumKey = except.getFieldError().getDefaultMessage();
        ErrorCode errorCode = ErrorCode.INVALID_KEY;
        try {
            errorCode = ErrorCode.valueOf(enumKey);
        } catch(IllegalArgumentException e){

        }
        ApiResponse apiResponse = new ApiResponse();
        apiResponse.setCode(errorCode.getCode());
        apiResponse.setMessage(errorCode.getMessage());
        return ResponseEntity.badRequest().body(apiResponse);
    }
}
```

---

## 2. GIẢI THÍCH CHI TIẾT CƠ CHẾ VẬN HÀNH

### 2.1. `@ControllerAdvice` là gì?
- Là một bộ lắng nghe toàn cục (Global Interceptor) hoạt động dựa trên cơ chế **AOP (Aspect-Oriented Programming)**.
- Thay vì ở từng Controller phải viết các khối lệnh `try - catch` lặp đi lặp lại rất xấu code, mọi ngoại lệ văng ra từ bất kỳ Controller nào sẽ ngay lập tức bị `GlobalExceptionHandler` "chặn đầu" và chuyển đổi thành thông điệp JSON chuẩn mực.

---

### 2.2. Cơ chế 3 tầng bắt lỗi:
1. **Tầng 1: Ngoại lệ nghiệp vụ (`AppException`)**:
   - Khi ở Service xảy ra sai sót logic, ví dụ: `throw new AppException(ErrorCode.PASSWORD_INCORRECT);`
   - Phương thức `handlingAppException` lập tức bắt được, đọc mã lỗi `1007` và chuỗi `"Mật khẩu cũ không chính xác"`, gói vào `ApiResponse` và gửi về Client với mã HTTP 400 Bad Request.
2. **Tầng 2: Ngoại lệ Validate DTO (`MethodArgumentNotValidException`)**:
   - Khi DTO khai báo `@Size(min = 8, message = "INVALID_PASSWORD")` mà người dùng chỉ nhập 4 ký tự.
   - Spring ném ra `MethodArgumentNotValidException`. Hàm `handlingValidation` lấy ra chuỗi message `"INVALID_PASSWORD"` và dùng `ErrorCode.valueOf("INVALID_PASSWORD")` để tìm mã lỗi 1004.
3. **Tầng 3: Lưới an toàn cuối cùng (`Exception.class`)**:
   - Nếu xảy ra lỗi bất ngờ ngoài dự kiến (như mất điện CSDL, lỗi kết nối mạng), hàm `handlingException` sẽ bắt lấy và trả về mã `9999` ("Uncategorized error"), không bao giờ để lộ thông tin cấu trúc code (Stacktrace) ra ngoài, bảo vệ an ninh tuyệt đối cho hệ thống.

---

## 3. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN & TRẢ LỜI ĐIỂM 10

### Câu 1: Tại sao `AppException` lại kế thừa `RuntimeException` mà không kế thừa `Exception`?
- **Trả lời**:
  > "Thưa thầy/cô:
  > - Trong Java, `Exception` là loại **Checked Exception** (bắt buộc phải khai báo `throws` ở chữ ký hàm hoặc phải bọc trong khối `try-catch`). Nếu dùng Checked Exception, mọi phương thức từ Repository, Service đến Controller đều phải khai báo `throws AppException`, làm code bị phụ thuộc và rất cồng kềnh.
  > - Ngược lại, `RuntimeException` là **Unchecked Exception**. Khi xảy ra lỗi, nó tự động văng ngược lên các tầng trên mà không bắt buộc phải khai báo `throws`. Spring Boot sẽ tự động bắt lấy tại `GlobalExceptionHandler` và thực hiện rollback giao dịch `@Transactional` một cách tự động."

### Câu 2: Ưu điểm của việc quản lý mã lỗi tập trung trong `ErrorCode` là gì?
- **Trả lời**:
  > "Thưa thầy/cô, việc dùng Enum `ErrorCode`:
  > 1. Tránh việc hard-code mã số và câu chữ rải rác ở khắp các file Java.
  > 2. Đảm bảo tính nhất quán: Cùng một lỗi 'Sai mật khẩu' sẽ luôn luôn mang mã số `1007` ở mọi nơi trong dự án.
  > 3. Hỗ trợ đa ngôn ngữ (i18n): Sau này nếu muốn chuyển từ tiếng Anh sang tiếng Việt, chúng em chỉ cần sửa duy nhất một chỗ trong file Enum `ErrorCode` mà không phải sửa hàng ngàn dòng code nghiệp vụ."
