import json, sys
sys.stdout.reconfigure(encoding='utf-8')

p6_passages_vi = {
    "131_134": (
        "Kính gửi toàn thể nhân viên,\n"
        "Tôi có tin tức muốn chia sẻ về một sự thay đổi [131] trong phòng nhân sự. "
        "Sau gần 20 năm gắn bó với Cometti Creative, cô Florence Shawn đã quyết định nghỉ hưu khỏi vị trí giám đốc nhân sự. "
        "Quản lý cấp cao hiện tại của phòng nhân sự chúng ta, anh Makoto Ichise, sẽ thay thế cô Shawn khi cô nghỉ hưu. "
        "Cô Shawn [132] đã luôn cố vấn, dìu dắt anh Ichise kể từ khi anh gia nhập công ty cách đây 5 năm. "
        "Ngày làm việc [133] cuối cùng của cô Shawn sẽ là ngày 22 tháng 2. "
        "Một bữa tiệc chia tay nghỉ hưu sẽ được tổ chức cho cô vào ngày hôm đó lúc 4:00 chiều tại Tiền sảnh Terey. "
        "[134] Chúng tôi rất hy vọng tất cả các bạn đều có thể tham dự để gửi lời chúc tốt đẹp nhất tới cô ấy.\n"
        "Thân ái,\nYoreli Costa\nGiám đốc Vận hành, Cometti Creative"
    ),
    "135_138": (
        "Bất động sản Lovitt – Giúp các gia đình tại Manitoba tìm thấy ngôi nhà mơ ước!\n"
        "Manuel Lovitt, [135] chủ sở hữu của Bất động sản Lovitt, đã có hơn 17 năm kinh nghiệm bán bất động sản. "
        "Ông Lovitt và đội ngũ từng đoạt giải thưởng của mình [136] chuyên về các ngôi nhà dành cho gia đình tại các khu vực Winnipeg, Brandon và Dauphin. "
        "Họ am hiểu tường tận về các trường học, công viên, dịch vụ tiện ích, giao thông và các hoạt động nâng cao chất lượng đời sống gia đình tại khu vực mà bạn muốn định cư. "
        "[137] Đó là bởi vì họ sinh sống ngay tại những cộng đồng mà họ phục vụ. "
        "Hãy liên hệ với Bất động sản Lovitt ngay hôm nay và để đội ngũ của chúng tôi dẫn lối bạn [138] hướng tới ngôi nhà trong mơ của bạn. "
        "Họ sẽ lắng nghe nhu cầu của bạn, thay mặt bạn đàm phán và giúp bạn sở hữu ngôi nhà tuyệt vời nhất xứng đáng với đồng tiền mồ hôi công sức của bạn.\n"
        "Gọi số 431-555-0168 để trao đổi với chuyên viên hoặc truy cập www.lovittrealestate.ca để biết thêm thông tin."
    ),
    "139_142": (
        "Chào mừng quý vị đến với chuyên đề 'Phân bổ tiền tiết kiệm của bạn'. "
        "Bài thuyết trình [139] bằng slide này là phần thứ ba trong chuỗi 12 phần giáo dục chuyên đề mang tên 'Chuẩn bị cho việc nghỉ hưu'. "
        "[140] Chuỗi chuyên đề này được thiết kế để giúp bạn đưa ra các quyết định tài chính sáng suốt. "
        "Chuyên đề này chỉ cung cấp lời khuyên [141] mang tính bổ trợ. "
        "Nội dung này không nên thay thế cho sự hướng dẫn từ chuyên viên hoạch định đầu tư của bạn. "
        "Chuỗi chuyên đề được phát triển như tài liệu nền tảng nhằm giúp bạn đặt ra các câu hỏi then chốt khi [142] tham khảo ý kiến chuyên viên hoạch định đầu tư của mình. "
        "Chúng tôi hy vọng bạn thấy thông tin này hữu ích.\n"
        "Swainson-Gray Investments"
    ),
    "143_146": (
        "Kính gửi Bác sĩ Paulwell,\n"
        "Thư này nhằm phản hồi cuộc họp nhân viên ngày hôm qua, đặc biệt là cuộc thảo luận về việc một số khía cạnh của phòng khám có thể ảnh hưởng đến công việc và sứ mệnh của chúng ta. "
        "[143] Tôi muốn đưa ra một đề xuất về chủ đề này. "
        "Hiện tại, các máy bán hàng tự động ở hành lang bên ngoài phòng chờ của chúng ta chứa đầy các sản phẩm nhiều đường và muối như nước ngọt có ga và bim bim. "
        "Là một đơn vị cung cấp dịch vụ y tế chăm sóc sức khỏe, chúng ta [144] nên cung cấp các loại đồ uống và đồ ăn nhẹ thể hiện cam kết của mình đối với việc giữ gìn sức khỏe. "
        "[145] Rốt cuộc thì, sứ mệnh cốt lõi của chúng ta luôn tập trung vào sức khỏe tốt. "
        "Tôi đã đính kèm một bài báo về các biện pháp mà các trung tâm y tế tương tự như chúng ta đang thực hiện để cải thiện các trạm phục vụ đồ ăn thức uống. "
        "Tôi hy vọng bác sĩ sẽ thấy tài liệu này [146] hữu ích. Bài viết nêu chi tiết một số thay đổi dễ thực hiện và tiết kiệm chi phí mà chúng ta có thể cân nhắc.\n"
        "Trân trọng,\nSilas Laveau"
    )
}

p6_questions_vi = {
    "131": {
        "qVi": "Chọn phương án thích hợp nhất cho chỗ trống [131]:",
        "optVi": {
            "A": "(A) sự khác biệt",
            "B": "(B) chiến lược",
            "C": "(C) sự thay đổi",
            "D": "(D) thói quen / sự luyện tập"
        }
    },
    "132": {
        "qVi": "Chọn phương án thích hợp nhất cho chỗ trống [132]:",
        "optVi": {
            "A": "(A) cố vấn (động từ thì hiện tại đơn)",
            "B": "(B) đang cố vấn (hiện tại tiếp diễn)",
            "C": "(C) sẽ cố vấn (tương lai đơn)",
            "D": "(D) đã và đang cố vấn (hiện tại hoàn thành tiếp diễn)"
        }
    },
    "133": {
        "qVi": "Chọn phương án thích hợp nhất cho chỗ trống [133]:",
        "optVi": {
            "A": "(A) cuối cùng",
            "B": "(B) ban đầu / nguyên bản",
            "C": "(C) linh hoạt",
            "D": "(D) thay thế luân phiên"
        }
    },
    "134": {
        "qVi": "Chọn phương án thích hợp nhất cho chỗ trống [134]:",
        "optVi": {
            "A": "(A) Cometti Creative sẽ sớm tuyển dụng người thay thế.",
            "B": "(B) Chúng tôi rất hy vọng tất cả các bạn có thể tham dự để gửi lời chúc tốt đẹp tới cô ấy.",
            "C": "(C) Cô Shawn là giám đốc nhân sự đầu tiên tại Cometti Creative.",
            "D": "(D) Dự án đầu tiên sẽ là việc tạo ra một chương trình phát triển tài năng."
        }
    },
    "135": {
        "qVi": "Chọn phương án thích hợp nhất cho chỗ trống [135]:",
        "optVi": {
            "A": "(A) sở hữu (động từ nguyên mẫu)",
            "B": "(B) đã sở hữu (quá khứ)",
            "C": "(C) người chủ / chủ sở hữu (danh từ)",
            "D": "(D) việc sở hữu (danh động từ)"
        }
    },
    "136": {
        "qVi": "Chọn phương án thích hợp nhất cho chỗ trống [136]:",
        "optVi": {
            "A": "(A) hành nghề / thực hành",
            "B": "(B) chuyên về (specialize in)",
            "C": "(C) báo cáo",
            "D": "(D) mua hàng"
        }
    },
    "137": {
        "qVi": "Chọn phương án thích hợp nhất cho chỗ trống [137]:",
        "optVi": {
            "A": "(A) Họ có thể sắp xếp phương tiện di chuyển cho trường tiểu học địa phương của bạn.",
            "B": "(B) Đó là bởi vì họ sinh sống ngay trong những cộng đồng mà họ phục vụ.",
            "C": "(C) Họ sẽ đóng cửa vào mùa hè nhưng sẽ sớm quay trở lại.",
            "D": "(D) Do đó, họ có thể giúp bạn đáp ứng mọi nhu cầu về ngân hàng."
        }
    },
    "138": {
        "qVi": "Chọn phương án thích hợp nhất cho chỗ trống [138]:",
        "optVi": {
            "A": "(A) hướng tới / về phía (giới từ chỉ hướng)",
            "B": "(B) sửa chữa",
            "C": "(C) bởi vì",
            "D": "(D) dọc theo"
        }
    },
    "139": {
        "qVi": "Chọn phương án thích hợp nhất cho chỗ trống [139]:",
        "optVi": {
            "A": "(A) việc trình bày (V-ing)",
            "B": "(B) trình bày (V-s)",
            "C": "(C) bài thuyết trình (danh từ ghép: slide presentation)",
            "D": "(D) đã được trình bày (V-ed)"
        }
    },
    "140": {
        "qVi": "Chọn phương án thích hợp nhất cho chỗ trống [140]:",
        "optVi": {
            "A": "(A) Bạn được khuyến khích đến văn phòng của chúng tôi để đánh giá danh mục đầu tư miễn phí.",
            "B": "(B) Chuỗi chuyên đề này được thiết kế để giúp bạn đưa ra các quyết định tài chính sáng suốt.",
            "C": "(C) Vui lòng điền vào các giấy tờ trước cuộc hẹn của bạn.",
            "D": "(D) Phản hồi của bạn sẽ giúp chúng tôi phục vụ bạn tốt hơn trong tương lai."
        }
    },
    "141": {
        "qVi": "Chọn phương án thích hợp nhất cho chỗ trống [141]:",
        "optVi": {
            "A": "(A) thuộc về khu vực",
            "B": "(B) đắt đỏ",
            "C": "(C) bổ sung / mang tính bổ trợ",
            "D": "(D) vui vẻ / đùa nghịch"
        }
    },
    "142": {
        "qVi": "Chọn phương án thích hợp nhất cho chỗ trống [142]:",
        "optVi": {
            "A": "(A) tham khảo ý kiến / tư vấn (consulting with)",
            "B": "(B) kê đơn thuốc",
            "C": "(C) liệt kê",
            "D": "(D) đi theo / tuân theo"
        }
    },
    "143": {
        "qVi": "Chọn phương án thích hợp nhất cho chỗ trống [143]:",
        "optVi": {
            "A": "(A) Tôi nghĩ cuộc họp đã kéo dài hơn mức cần thiết.",
            "B": "(B) Tôi ước gì chúng ta đã được thông báo về việc đó sớm hơn.",
            "C": "(C) Tôi muốn đưa ra một đề xuất về chủ đề này.",
            "D": "(D) Tôi rất vinh dự nếu được chủ trì một phiên họp tiếp theo."
        }
    },
    "144": {
        "qVi": "Chọn phương án thích hợp nhất cho chỗ trống [144]:",
        "optVi": {
            "A": "(A) sẽ cung cấp (will offer)",
            "B": "(B) đã cung cấp (have offered)",
            "C": "(C) đã đang cung cấp (were offering)",
            "D": "(D) nên cung cấp (should be offering - thể hiện lời khuyên / nghĩa vụ)"
        }
    },
    "145": {
        "qVi": "Chọn phương án thích hợp nhất cho chỗ trống [145]:",
        "optVi": {
            "A": "(A) Rốt cuộc thì / Xét cho cùng (After all)",
            "B": "(B) Nhân tiện / Tiện thể",
            "C": "(C) Trong lúc chờ đợi",
            "D": "(D) Mặt khác"
        }
    },
    "146": {
        "qVi": "Chọn phương án thích hợp nhất cho chỗ trống [146]:",
        "optVi": {
            "A": "(A) hữu ích",
            "B": "(B) có nhiều sự kiện quan trọng",
            "C": "(C) sinh lời",
            "D": "(D) thoải mái"
        }
    }
}

with open('scratch/t3_p6_bilingual.json', 'w', encoding='utf-8') as f:
    json.dump({
        "p6_passages_vi": p6_passages_vi,
        "p6_questions_vi": p6_questions_vi
    }, f, ensure_ascii=False, indent=2)

print("Generated scratch/t3_p6_bilingual.json successfully!")
