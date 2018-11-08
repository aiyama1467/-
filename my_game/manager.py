class CollisionManager:
    def check_collision(self, ball, block, ball_size, block_size):
        if block.x <= ball.x <= block.x + block_size.x:
            if block.y <= ball.y <= block.y + block_size.y:
                return True, 0
            elif block.y <= ball.y + ball_size.y <= block.y + block_size.y:
                return True, 0
        elif ball.x <= block.x <= ball.x + ball_size.x:
            if ball.y <= block.y <= ball.y + ball_size.y:
                return True, 1
            elif ball.y <= block.y + block_size.y <= ball.y + ball_size.y:
                return True, 1

        return False, -1

    def is_collition_ball_blocks(self, ball, blocks):
        for block_l in blocks.blocks:
            for block in block_l:
                if block.is_Exist:
                    b, s = self.check_collision(ball.pos, block.pos, ball.size, block.size)
                    if b:
                        block.is_Exist = False
                        if s == 0:
                            ball.direction.y = -ball.direction.y
                        else:
                            ball.direction.x = -ball.direction.x

        return False

    def is_collition_ball_bar(self, ball, bar):
        if self.check_collision(ball.pos, bar.pos, ball.size, bar.size)[0]:
            ball.direction.y = -ball.direction.y

    def is_collision_ball_wall(self, ball, wsize):
        if ball.pos.y < 0:
            ball.direction.y = -ball.direction.y
        elif ball.pos.x < 0 or ball.pos.x + ball.size.x > wsize.x:
            ball.direction.x = -ball.direction.x
        elif ball.pos.y > wsize.y:
            return True
