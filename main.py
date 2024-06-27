from deuces import Card, Evaluator

# Создание карт на борде и в руке
board = [Card.new('2h'), Card.new('3d'), Card.new('5s'), Card.new('9c'), Card.new('Kd')]
hand = [Card.new('Ah'), Card.new('Qh')]

# Создание оценщика
evaluator = Evaluator()
rank = evaluator.evaluate(board, hand)
hand_class = evaluator.get_rank_class(rank)

# Вывод результатов
print(f"Hand rank: {rank}")
print(f"Hand class: {hand_class}")

# Строковые представления всех карт
values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
suits = ['h', 'd', 'c', 's']
all_cards = [value + suit for value in values for suit in suits]
print(all_cards)

# Функция для создания карты из строкового представления
def create_card(card_str):
    return Card.new(card_str)

# Функция для оценки силы руки
def evaluate_hand(board_str, hand_str):
    board = [create_card(card) for card in board_str]
    hand = [create_card(card) for card in hand_str]

    evaluator = Evaluator()
    rank = evaluator.evaluate(board, hand)
    hand_class = evaluator.get_rank_class(rank)
    hand_class_name = evaluator.class_to_string(hand_class)

    return rank, hand_class, hand_class_name

# Пример использования
board_str = ['2h', '3d', '5s', '9c', 'Kd']
hand_str = ['Ah', 'Ad']

rank, hand_class, hand_class_name = evaluate_hand(board_str, hand_str)
print(f"Hand rank: {rank}")
print(f"Hand class: {hand_class}")
print(f"Hand class name: {hand_class_name}")
