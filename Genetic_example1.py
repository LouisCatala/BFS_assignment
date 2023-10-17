import random

def fitness(chromosome):
    return sum(gene for gene in chromosome)

def select_parents(population):
    total_fitness = sum(fitness(chrom) for chrom in population)
    selection_probs = [fitness(chrom)/total_fitness for chrom in population]
    parents = random.choices(population, weights=selection_probs, k=2)
    return parents

def crossover(parent1, parent2):
    crossover_point = len(parent1) // 2
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(chromosome):
    mutation_point = random.randint(0, len(chromosome) - 1)
    chromosome[mutation_point] = round(random.uniform(0, 1), 2)
    return chromosome

# Example 1 initial inputs in Chapter 2 slides
population = [[0.51, 0.33, 0.02, 0.48],
              [0.11, 0.64, 0.31, 0.31],
              [0.72, 0.99, 0.82, 0.25]]
              
print(f"Input Parents:")
for parent in population:
    print(parent)

parents = select_parents(population)
print(f"\nSelected Parents:")
for parent in parents:
    print(parent)

child1, child2 = crossover(parents[0], parents[1])
print(f"\nChildren before Mutation:")
print(child1)
print(child2)

if random.random() < 0.1:  # Assuming 10% mutation rate
    child1 = mutate(child1)
if random.random() < 0.1:
    child2 = mutate(child2)

print(f"\nChildren after Mutation:")
print(child1)
print(child2)

best_chromosome = max(population, key=fitness)
print(f"\nNew Generation:")
new_generation = [best_chromosome, child1, child2]
for chrom in new_generation:
    print(chrom)
