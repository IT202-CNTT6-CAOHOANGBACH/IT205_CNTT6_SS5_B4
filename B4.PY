chi_nhanh = int(input("Nhập số lượng chi nhánh: "))
for i in range(1,chi_nhanh+1):
    print(f'chi nhanh{i}:')
    for class_std in range(1,3):
        flag = True
        while flag:
            hoc_vien = int(input(f'nhap so luong học viên lớp{class_std} '))
            if hoc_vien <0:
                print('Số học viên không hợp lệ. Vui lòng nhập lại.')
                continue
            elif hoc_vien == 0:
                print('Lớp vắng toàn bộ. Bỏ qua kiểm tra trạng thái.')
                break;
            else:
                flag = False
        if hoc_vien >20:
            print(f'Chi nhánh{i} - Lớp {class_std}Lớp học ổn định')
        elif  hoc_vien <=20 and hoc_vien >0 :
            print(f'Chi nhánh{i} - Lớp {class_std}lớp cần được nhắc nhở theo dõi')
            