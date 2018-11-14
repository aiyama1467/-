class CollisionManager:
    def check_collision(self, ball, block):
        if block.pos.x <= ball.pos.x <= block.pos.x + block.size.x:
            if block.pos.y <= ball.pos.y <= block.pos.y + block.size.y:
                return True
            elif block.pos.y <= ball.pos.y + ball.size.y <= block.pos.y + block.size.y:
                return True

        elif ball.pos.x <= block.pos.x <= ball.pos.x + ball.size.x:
            if ball.pos.y <= block.pos.y <= ball.pos.y + ball.size.y:
                return True
            elif ball.pos.y <= block.pos.y + block.size.y <= ball.pos.y + ball.size.y:
                return True

        return False

    def is_collition_ball_blocks(self, ball, blocks):
        for block_l in blocks.blocks:
            for block in block_l:
                if block.is_Exist:

                    if self.check_collision(ball, block):
                        block.is_Exist = False
                        if block.pos.y + block.size.y <= ball.bpos.y or block.pos.y >= ball.bpos.y:
                            ball.direction.y = -ball.direction.y
                            ball.is_collided = True
                        elif block.pos.y <= ball.bpos.y <= block.pos.y + block.size.y:
                            ball.direction.x = -ball.direction.x
                            ball.is_collided = True

        return False

    def is_collition_ball_bar(self, ball, bar):
        if self.check_collision(ball, bar):
            ball.direction.y = -ball.direction.y
            ball.is_collided = True

    def is_collision_ball_wall(self, ball, wsize):
        if ball.pos.y < 0:
            ball.direction.y = -ball.direction.y
            ball.is_collided = True
        elif ball.pos.x < 0 or ball.pos.x + ball.size.x > wsize.x:
            ball.direction.x = -ball.direction.x
            ball.is_collided = True
        elif ball.pos.y > wsize.y:
            return True
