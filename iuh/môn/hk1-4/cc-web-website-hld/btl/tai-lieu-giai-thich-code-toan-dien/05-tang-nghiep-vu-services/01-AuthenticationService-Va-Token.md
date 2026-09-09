# GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE TRONG AUTHENTICATIONSERVICE

> **Mục tiêu**: Hiểu bản chất 100% cơ chế xác thực không trạng thái (Stateless Authentication) bằng **JSON Web Token (JWT)**, thuật toán mã hóa chữ ký số **HMAC-SHA512**, cách băm và so khớp mật khẩu bằng **BCrypt**, và phương thức kiểm tra tính hợp lệ của Token (`introspect`).

---

## 1. MÃ NGUỒN ĐẦY ĐỦ CỦA `AuthenticationService.java`

File nằm tại: `src/main/java/com/group/blog/service/AuthenticationService.java`

```java
package com.group.blog.service;

import com.group.blog.dto.request.AuthenticationRequest;
import com.group.blog.dto.request.IntrospectRequest;
import com.group.blog.dto.response.AuthenticationResponse;
import com.group.blog.dto.response.IntrospectResponse;
import com.group.blog.entity.User;
import com.group.blog.exception.AppException;
import com.group.blog.exception.ErrorCode;
import com.group.blog.repository.UserRepository;
import com.nimbusds.jose.*;
import com.nimbusds.jose.crypto.MACSigner;
import com.nimbusds.jose.crypto.MACVerifier;
import com.nimbusds.jwt.JWTClaimsSet;
import com.nimbusds.jwt.SignedJWT;
import lombok.AccessLevel;
import lombok.RequiredArgsConstructor;
import lombok.experimental.FieldDefaults;
import lombok.experimental.NonFinal;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.util.CollectionUtils;

import java.text.ParseException;
import java.time.Instant;
import java.time.temporal.ChronoUnit;
import java.util.Date;
import java.util.StringJoiner;

@Slf4j
@Service
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class AuthenticationService {
    UserRepository userRepository;
    PasswordEncoder passwordEncoder;

    @NonFinal
    @Value("${jwt.signerKey}")
    protected String SIGNER_KEY;

    public AuthenticationResponse authenticate(AuthenticationRequest request){
        Date expiryTime = new Date(Instant.now().plus(1, ChronoUnit.HOURS).toEpochMilli());
        var user = userRepository.findByUsername(request.getUsername())
                .orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXITED));

        boolean authenticated = passwordEncoder.matches(request.getPassword(), user.getPassword());
        if(!authenticated) throw new AppException(ErrorCode.UNAUTHENTICATED);

        var token = generateToken(user, expiryTime);
        return AuthenticationResponse.builder()
                .token(token)
                .authenticated(true)
                .expiryTime(expiryTime)
                .build();
    }

    private String generateToken(User user, Date expiryTime){
        JWSHeader header = new JWSHeader(JWSAlgorithm.HS512);
        JWTClaimsSet jwtClaimsSet = new JWTClaimsSet.Builder()
                .subject(user.getUsername())
                .issuer("group.com")
                .issueTime(new Date())
                .expirationTime(expiryTime)
                .claim("scope", buildScope(user))
                .build();
        Payload payload = new Payload(jwtClaimsSet.toJSONObject());
        JWSObject jwsObject = new JWSObject(header, payload);
        try {
            jwsObject.sign(new MACSigner(SIGNER_KEY.getBytes()));
            return jwsObject.serialize();
        } catch (JOSEException e) {
            log.error("Cannot create token", e);
            throw new RuntimeException(e);
        }
    }

    private String buildScope(User user){
        StringJoiner stringJoiner = new StringJoiner(" ");
        if(!CollectionUtils.isEmpty(user.getRoles()))
            user.getRoles().forEach(stringJoiner::add);
        return stringJoiner.toString();
    }

    public IntrospectResponse introspect(IntrospectRequest request) {
        var token = request.getToken();
        boolean isValid = false;
        try {
            JWSVerifier verifier = new MACVerifier(SIGNER_KEY.getBytes());
            SignedJWT signedJWT = SignedJWT.parse(token);
            Date expiryTime = signedJWT.getJWTClaimsSet().getExpirationTime();
            var verified = signedJWT.verify(verifier);
            isValid = verified && expiryTime != null && expiryTime.after(new Date());
        } catch (ParseException | JOSEException | IllegalArgumentException e) {
            log.warn("Token invalid: {}", e.getMessage());
        }
        return IntrospectResponse.builder()
                .valid(isValid)
                .build();
    }
}
```

---

## 2. GIẢI THÍCH CHI TIẾT TỪNG DÒNG VÀ TỪNG PHƯƠNG THỨC

### 2.1. Các Annotation và Tiêm phụ thuộc (Dependency Injection)
```java
@Slf4j
@Service
@RequiredArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE, makeFinal = true)
public class AuthenticationService {
    UserRepository userRepository;
    PasswordEncoder passwordEncoder;

    @NonFinal
    @Value("${jwt.signerKey}")
    protected String SIGNER_KEY;
```
- **`@Slf4j`**: Tự động sinh biến `log` để in thông báo lỗi ra màn hình Console.
- **`@RequiredArgsConstructor` & `makeFinal = true`**: Đây là chuẩn thiết kế hiện đại nhất của Spring: **Constructor-based Injection**. Mọi trường có từ khóa `final` sẽ được Lombok tự động gom vào Constructor để Spring tự động tiêm đối tượng vào. Không cần phải viết hàng loạt `@Autowired` thủ công!
- **`@NonFinal` trên `SIGNER_KEY`**: Vì `SIGNER_KEY` được tiêm giá trị từ file YAML qua `@Value("${jwt.signerKey}")` tại thời điểm sau khi đối tượng được tạo, nên trường này không được phép là `final`.

---

### 2.2. Phương thức Xác thực Đăng nhập `authenticate()`
```java
    public AuthenticationResponse authenticate(AuthenticationRequest request){
        Date expiryTime = new Date(Instant.now().plus(1, ChronoUnit.HOURS).toEpochMilli());
```
- Đặt thời hạn sống của Token là **1 giờ** tính từ thời điểm đăng nhập (`Instant.now().plus(1, ChronoUnit.HOURS)`). Sau 1 giờ, token sẽ tự động hết hạn, người dùng phải đăng nhập lại để đảm bảo an toàn nếu chẳng may bị lộ máy tính.

```java
        var user = userRepository.findByUsername(request.getUsername())
                .orElseThrow(() -> new AppException(ErrorCode.USER_NOT_EXITED));
```
- Lấy thông tin user từ CSDL. Nếu không tìm thấy tên đăng nhập này, ném lỗi `USER_NOT_EXITED` (Mã lỗi 1005).

```java
        boolean authenticated = passwordEncoder.matches(request.getPassword(), user.getPassword());
        if(!authenticated) throw new AppException(ErrorCode.UNAUTHENTICATED);
```
- **Hàm `passwordEncoder.matches(rawPassword, encodedPassword)`**: So khớp mật khẩu người dùng nhập với chuỗi băm trong DB.
  - **Lưu ý vấn đáp cực kỳ quan trọng**: Tuyệt đối không thể dùng `rawPassword.equals(user.getPassword())` vì trong DB mật khẩu là chuỗi băm BCrypt (`$2a$10$...`). Thuật toán BCrypt có chứa muối ngẫu nhiên (salt), hàm `matches` sẽ tự trích xuất muối và băm lại mật khẩu nhập vào để so khớp an toàn.
  - Nếu sai mật khẩu, ném ngoại lệ `UNAUTHENTICATED` (Mã lỗi 1006 - HTTP 401).

```java
        var token = generateToken(user, expiryTime);
        return AuthenticationResponse.builder()
                .token(token)
                .authenticated(true)
                .expiryTime(expiryTime)
                .build();
```
- Tạo chuỗi token JWT và đóng gói trả về cho Client.

---

### 2.3. Thuật toán sinh Token `generateToken()` và Cấu trúc 3 phần của JWT
```java
    private String generateToken(User user, Date expiryTime){
        JWSHeader header = new JWSHeader(JWSAlgorithm.HS512);
```
- **Phần 1: Header của JWT**: Khai báo thuật toán mã hóa chữ ký là `HS512` (HMAC sử dụng hàm băm SHA-512).

```java
        JWTClaimsSet jwtClaimsSet = new JWTClaimsSet.Builder()
                .subject(user.getUsername())
                .issuer("group.com")
                .issueTime(new Date())
                .expirationTime(expiryTime)
                .claim("scope", buildScope(user))
                .build();
```
- **Phần 2: Payload (Nội dung dữ liệu của Token)**:
  - `subject`: Định danh chủ sở hữu token chính là `username` của người dùng.
  - `issuer`: Tên tổ chức phát hành token (`group.com`).
  - `issueTime`: Thời điểm cấp token.
  - `expirationTime`: Thời điểm token hết hạn.
  - `claim("scope", ...)`: Chứa các quyền hạn của user, được nối với nhau bằng dấu cách (Ví dụ: `"ADMIN USER"`). Spring Security sẽ đọc trường `scope` này để phân quyền API!

```java
        Payload payload = new Payload(jwtClaimsSet.toJSONObject());
        JWSObject jwsObject = new JWSObject(header, payload);
        try {
            jwsObject.sign(new MACSigner(SIGNER_KEY.getBytes()));
            return jwsObject.serialize();
        } catch (JOSEException e) {
            log.error("Cannot create token", e);
            throw new RuntimeException(e);
        }
    }
```
- **Phần 3: Signature (Chữ ký số)**:
  - Lấy phần Header và phần Payload, kết hợp cùng chuỗi bí mật `SIGNER_KEY` rồi băm qua thuật toán HMAC-SHA512.
  - Hàm `serialize()` sẽ ghép 3 phần lại với nhau bằng dấu chấm `.` tạo thành chuỗi JWT hoàn chỉnh:
    ```
    xxxxx.yyyyy.zzzzz
    (Header).(Payload).(Signature)
    ```

---

### 2.4. Phương thức Kiểm tra Token `introspect()`
```java
    public IntrospectResponse introspect(IntrospectRequest request) {
        var token = request.getToken();
        boolean isValid = false;
        try {
            JWSVerifier verifier = new MACVerifier(SIGNER_KEY.getBytes());
            SignedJWT signedJWT = SignedJWT.parse(token);
            Date expiryTime = signedJWT.getJWTClaimsSet().getExpirationTime();
            var verified = signedJWT.verify(verifier);
            isValid = verified && expiryTime != null && expiryTime.after(new Date());
        } catch (ParseException | JOSEException | IllegalArgumentException e) {
            log.warn("Token invalid: {}", e.getMessage());
        }
        return IntrospectResponse.builder().valid(isValid).build();
    }
```
- Được gọi khi Frontend muốn kiểm tra xem phiên đăng nhập hiện tại còn sống hay đã chết:
  1. `signedJWT.verify(verifier)`: Kiểm tra xem chữ ký số có đúng do server ký bằng `SIGNER_KEY` không. Nếu hacker sửa `username` trong Payload từ `user` thành `admin`, chữ ký sẽ bị lệch và trả về `false`.
  2. `expiryTime.after(new Date())`: Kiểm tra xem thời hạn của token có lớn hơn thời điểm hiện tại không.
  3. Bắt các ngoại lệ định dạng sai (token rác, thiếu dấu chấm) để không bao giờ làm sập ứng dụng (văng lỗi 500), mà chỉ trả về `valid: false`.

---

## 3. CÂU HỎI VẤN ĐÁP CỦA GIẢNG VIÊN VỀ AUTHENTICATION & JWT

### Câu 1: Em hãy trình bày cấu trúc của một chuỗi JWT Token? Nếu một người dùng sửa thông tin trong Token ở trình duyệt thì Server có phát hiện được không?
- **Trả lời**:
  > "Thưa thầy/cô, một chuỗi JWT gồm đúng 3 phần ngăn cách nhau bằng dấu chấm:
  > 1. **Header**: Chứa thuật toán mã hóa (ở đây là HS512).
  > 2. **Payload**: Chứa các thông tin định danh (subject là username, hạn sử dụng, và claim scope chứa quyền ADMIN/USER).
  > 3. **Signature (Chữ ký số)**: Được tạo ra bằng công thức: `HMAC_SHA512(Header + Payload, SecretKey)`.
  > 
  > Nếu một người dùng ở Client cố tình dùng công cụ giải mã Base64 để đổi quyền từ `USER` thành `ADMIN`, thì khi gửi token lên Server, Server sẽ dùng khóa bí mật `SIGNER_KEY` để tính toán lại chữ ký. Do Payload đã bị thay đổi, chữ ký mới tính ra sẽ không trùng khớp với chữ ký cũ đính kèm trong token. Phương thức `signedJWT.verify(verifier)` sẽ trả về `false` và Server lập tức chặn đứng yêu cầu đó!"

### Câu 2: Tại sao khi lưu mật khẩu vào Database, nhóm em lại dùng BCrypt mà không dùng MD5 hay SHA-256?
- **Trả lời**:
  > "Thưa thầy/cô:
  > - MD5 và SHA-256 là các hàm băm thông thường, có tốc độ tính toán quá nhanh và không tự sinh muối ngẫu nhiên (Salt). Hacker có thể dùng các bảng tra cứu sẵn (Rainbow Table) hoặc dùng card màn hình GPU để thử hàng tỷ mật khẩu mỗi giây và bẻ khóa rất dễ dàng.
  > - Ngược lại, **BCrypt** là thuật toán băm chậm thích ứng (Adaptive Hash Function). Nó tự động sinh ra một chuỗi muối ngẫu nhiên (Salt) dài 16 byte gộp vào trong chuỗi băm, khiến cho 2 người dùng có cùng mật khẩu '123456' thì chuỗi băm trong DB vẫn hoàn toàn khác nhau. Ngoài ra nó cho phép cấu hình độ khó (Cost Factor = 10 trong dự án của tụi em) để làm chậm tốc độ thử mật khẩu của hacker, chống lại triệt để tấn công vét cạn (Brute-force)."
