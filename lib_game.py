import pygame,copy
def handle_event_player(event,player_rect,laser_rect,lst_laser_rect):
        # Xử lý toạ độ chuột di chuyển
        if event.type == pygame.MOUSEMOTION:  # Hành động rê chuột
            x, y = event.pos  # (x,y) #Lấy ra toạ con trỏ chuột
            # chỉnh toạ máy bay về giữa trỏ chuột
            player_rect.x = x - player_rect.width // 2
            player_rect.y = y - player_rect.height // 2
        # Xử lý click chuột bắn lấy toạ độ xuất phát viên đạn = toạ độ của máy bay
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Cách 1: tạo ra bằng hàm pygame.Rect 1 hình chữ nhật mới
            # Tạo mới hoàn toàn viên đạn (rect viên đạn) sau mỗi lần click
            # x_laser = player_rect.x + player_rect.width/2
            # y_laser =  player_rect.y
            # new_laser_rect = pygame.Rect(x_laser,y_laser,laser.get_width(),laser.get_height())

            # Cách 2: Clone viên đạn rect ngoài vòng lặp game (dòng 18) bằng hàm copy deep
            new_laser_rect = copy.deepcopy(laser_rect)
            new_laser_rect.x = player_rect.x + player_rect.width/2
            new_laser_rect.y = player_rect.y
            # Lưu laser rect vao list
            # [laser_rect1,laser_rect2, laser_rect3]
            lst_laser_rect.append(new_laser_rect)
            
#Xử lý đạn
def handle_laser(SCREEN,laser,lst_laser_rect,lst_meteor,score):
   # Thay đổi toạ độ viên đạn sau mỗi khung hình và vẽ lại từng viên đạn sau mỗi lần vòng lặp game (while true chạy)
    for laser_rect_item in lst_laser_rect:
        laser_rect_item.y -= 10
        SCREEN.blit(laser, (laser_rect_item.x, laser_rect_item.y))
        #Xử lý xoá đạn khi đạn ra khỏi màn hình
        if laser_rect_item.y < 0:
            lst_laser_rect.remove(laser_rect_item)
        #Khi blit viên đạn xử lý bắn trúng
        #Duyệt list thiên thạch xem có thiên thạch nào chạm từng viên đạn hay ko
        for meteor_rect in lst_meteor:
            if laser_rect_item.colliderect(meteor_rect):
                #Xử lý bắn trúng => cộng điểm và xoá thiên thạch + đạn
                score += 100
                lst_meteor.remove(meteor_rect)
                lst_laser_rect.remove(laser_rect_item)
    #Giá trị primitive không bị thay đổi khi sử dụng hàm vì vậy khi xử lý xong cần lấy những giá trị này ra bên ngoài thì return thành kết quả (Nếu có nhiều kết quả thì có thể return tuple sau đó tại chỗ gọi hàm lấy ra xử lý)            
    return (score,123)