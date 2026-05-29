# Hệ thống đánh giá sĩ số lớp học

# Nhập số lượng chi nhánh
branch_count = int(input("Nhập số lượng chi nhánh: "))

# Duyệt từng chi nhánh
for branch in range(1, branch_count + 1):
    print(f"\nChi nhánh {branch}")
    
    # Mỗi chi nhánh có 2 lớp
    for classroom in range(1, 3):
        while True:
            student_count = int(input(f"Nhập số học viên đi học của lớp {classroom}: "))
            
            # Edge case 1: số học viên âm
            if student_count < 0:
                print("Số học viên không hợp lệ. Vui lòng nhập lại.")
                continue  # yêu cầu nhập lại
            
            # Edge case 2: lớp vắng toàn bộ
            if student_count == 0:
                print("Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.")
                break  # bỏ qua lớp này
            
            # Đánh giá trạng thái lớp học
            if student_count < 20:
                print(f"Chi nhánh {branch} - Lớp {classroom}: Lớp cần được nhắc nhở theo dõi")
            else:
                print(f"Chi nhánh {branch} - Lớp {classroom}: Lớp học ổn định")
            
            break  # thoát vòng while sau khi nhập hợp lệ
