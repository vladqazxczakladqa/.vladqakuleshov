def count_required_skills(skills_tree, required_skills):
    # создаем множество для хранения уже изученных навыков
    learned_skills = set()
    
    # создаем стек для обхода дерева навыков в глубину
    stack = []
    stack.append(0)
    
    # обходим дерево в глубину, добавляем каждый изученный навык в learned_skills
    while stack:
        current_skill = stack.pop()
        learned_skills.add(current_skill)
        
        # проверяем, есть ли у текущего навыка дочерние навыки
        if current_skill in skills_tree:
            for child_skill in skills_tree[current_skill]:
                stack.append(child_skill)
    
    # считаем количество необходимых навыков, которые еще не были изучены
    required_skills_count = 0
    for skill in required_skills:
        if skill not in learned_skills:
            required_skills_count += 1
    
    return required_skills_count