package b5;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;

public class DateTimeService {

   
    public static String handle(String req) {
        if (req == null) return "Nhap 1(Time) / 2(Date) / 3(Date&Time)";

        String s = req.trim();

        switch (s) {
            case "1":
            case "Time":
            case "time":
                return "Time: " + LocalTime.now();

            case "2":
            case "Date":
            case "date":
                return "Date: " + LocalDate.now();

            case "3":
            case "Date & Time":
            case "DateTime":
            case "datetime":
                return "Date&Time: " + LocalDateTime.now();

            default:
                return "Nhap 1(Time) / 2(Date) / 3(Date&Time)";
        }
    }
}