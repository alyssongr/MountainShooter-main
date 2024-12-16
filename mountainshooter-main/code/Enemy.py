from code.Const import ENTITY_SPEED, WIN_HEIGHT, ENTITY_SHOT_DELAY, ENTITY_SCORE
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

        if self.name == 'Enemy3':
            self.vertical_speed = ENTITY_SPEED[self.name]  # Velocidade vertical normal
            self.vertical_direction = 1  # 1 para baixo, -1 para cima
            self.vertical_timer = 0  # Timer para o movimento vertical
        else:
            self.vertical_speed = 0  # Inimigos que não são Enemy3 não têm movimento vertical

    def move(self):
        if self.name == 'Enemy3':
            # Movimento horizontal constante da direita para a esquerda
            self.rect.centerx -= ENTITY_SPEED[self.name]

            # Movimento vertical com oscilação
            self.rect.centery += self.vertical_speed * self.vertical_direction

            # Atualiza o timer para o movimento vertical
            self.vertical_timer += 1

            # Se o timer alcançar um determinado valor, inverta a direção vertical
            if self.vertical_timer > 60:  # Ajuste o valor conforme necessário
                if self.rect.top <= 0:
                    self.vertical_direction = 1  # Começa a descer
                    self.vertical_speed = ENTITY_SPEED[self.name] * 2  # Dobrar a velocidade para baixo
                elif self.rect.bottom >= WIN_HEIGHT:
                    self.vertical_direction = -1  # Começa a subir
                    self.vertical_speed = ENTITY_SPEED[self.name]  # Retorna a velocidade normal
                self.vertical_timer = 0  # Reinicia o timer

        else:
            # Movimento horizontal para outros inimigos
            self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay <= 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            shot_name = f'{self.name}Shot'
            # Verifica se o nome do tiro está no dicionário ENTITY_SCORE
            if shot_name not in ENTITY_SCORE:
                raise ValueError(f"Nome do tiro {shot_name} não encontrado em ENTITY_SCORE")
            return EnemyShot(name=shot_name, position=(self.rect.centerx, self.rect.centery))
