from dataclasses import dataclass, field


@dataclass
class Node:
    title: str
    children: list["Node"] = field(default_factory=list)


menu = Node("Головне меню", [
    Node("Файл", [
        Node("Новий", []),
        Node("Зберегти", []),
    ]),
    Node("Правка", [
        Node("Копіювати", []),
    ]),
    Node("Вигляд", [
        Node("Масштаб", [
            Node("Збільшити", []),
            Node("Зменшити", []),
        ]),
    ]),
    Node("Довідка", []),
])

callCount = 0


def printMenu(node: Node, level: int = 0) -> None:
    print("  " * level + node.title)
    for child in node.children:
        printMenu(child, level + 1)


def countItems(node: Node) -> int:
    global callCount
    callCount += 1
    total = 1
    for child in node.children:
        total += countItems(child)
    return total


def find(node: Node, name: str) -> bool:
    if node.title == name:
        return True
    for child in node.children:
        if find(child, name):
            return True
    return False


if __name__ == "__main__":
    printMenu(menu, 0)
    print()

    callCount = 0
    print(countItems(menu))
    print(callCount)
    print()

    print("так" if find(menu, "Зберегти") else "ні")
    print("так" if find(menu, "Масштаб") else "ні")
    print("так" if find(menu, "Довідка") else "ні")
    print("так" if find(menu, "Експорт") else "ні")