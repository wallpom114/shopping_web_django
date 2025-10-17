intents = {
    "greeting": {
        "patterns": [
            # Patterns có dấu
            "xin chào", "hello", "hi", "chào bạn", "alo",
            "good morning", "good afternoon", "good evening",
            # Patterns không dấu
            "xin chao", "chao ban", "chao", "xin", "hey"
        ],
        "responses": [
            "Xin chào! Tôi có thể giúp gì cho bạn?",
            "Chào bạn! Bạn cần hỗ trợ gì ạ?",
            "Chào mừng bạn đến với cửa hàng của chúng tôi!"
        ]
    },
    "price_query": {
        "patterns": [
            # Patterns có dấu
            "giá của", "giá bao nhiêu", "bao nhiêu tiền",
            "giá sản phẩm", "mắc không", "giá cả",
            # Patterns không dấu
            "gia cua", "gia bao nhieu", "bao nhieu tien",
            "gia san pham", "mac khong", "gia ca",
            "cho hoi gia", "bao nhieu mot"
        ]
    },
    "product_search": {
        "patterns": [
            # Patterns có dấu
            "tìm sản phẩm", "có bán", "bán không",
            "cần mua", "đang tìm", "muốn mua",
            "tìm kiếm", "tìm", "xem sản phẩm",
            # Patterns không dấu
            "tim san pham", "co ban", "ban khong",
            "can mua", "dang tim", "muon mua",
            "tim kiem", "tim", "xem san pham"
        ]
    },
    "best_seller": {
        "patterns": [
            # Patterns có dấu
            "sản phẩm bán chạy", "bán chạy nhất",
            "phổ biến nhất", "mua nhiều nhất", "hot nhất",
            # Patterns không dấu
            "san pham ban chay", "ban chay nhat",
            "pho bien nhat", "mua nhieu nhat", "hot nhat",
            "san pham hot", "ban tot nhat"
        ]
    }
}
