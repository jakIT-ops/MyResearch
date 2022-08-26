defmodule Genetic do
  alias Types.Chromosome

  def initialize(genotype, opts \\ []) do
    population_size = Keyword.get(opts, :population_size, 100)
    for _ <- 1..population_size, do: genotype.()
  end

  def evaluate(population, fitness_function, opts \\ []) do
    population
    |> Enum.map(
        fn chromosome ->
          fitness = fitness_function.(chromosome)
          age = chromosome.age + 1
          %Chromosome{chromosome | fitness: fitness, age: age}
        end
      )
    |> Enum.sort_by(fitness_function, &>=/2)
  end

  def select(population, opts \\ []) do
    select_fn = Keyword.get(opts, :selection_type, &Toolbox.Selection.elite/2)
    select_rate = Keyword.get(opts, :selection_rate, 0.8)
    n = round(length(population) * select_rate)
    n = if rem(n, 2) == 0, do: n, else: n+1
    parents =
      select_fn
      |> apply([population, n])
    leftover = MapSet.difference(MapSet.new(population), MapSet.new(parents))
    parents =
      parents
      |> Enum.chunk_every(2)
      |> Enum.map(& List.to_tuple(&1))
    {parents, MapSet.to_list(leftover)}
  end

  def crossover(population, opts \\ []) do
    crossover_fn = Keyword.get(opts, :crossover_type, &Toolbox.Crossover.single_point/2)
    population
    |> Enum.reduce([],
        fn {p1, p2}, acc ->
          {c1, c2} = apply(crossover_fn, [p1, p2])
          [c1 | [c2 | acc]]
        end
      )
  end

  def mutation(population, opts \\ []) do
    mutate_fn = Keyword.get(opts, :mutation_type, &Toolbox.Mutation.scramble/1)
    rate = Keyword.get(opts, :mutation_rate, 0.05)
    population
    |> Enum.map(
        fn chromosome ->
          if :rand.uniform() < rate do
            apply(mutate_fn, [chromosome])
          else
            chromosome
          end
        end
      )
  end

  def run(problem, opts \\ []) do
    population = initialize(&problem.genotype/0)
    population
    |> evolve(problem, 0, opts)
  end

  def evolve(population, problem, generation, opts \\ []) do
    population = evaluate(population, &problem.fitness_function/1, opts)
    best = hd(population)
    IO.write("\rCurrent best: #{best.fitness}")
    if problem.terminate?(population, generation) do
      best
    else
      {parents, leftover} = select(population, opts)
      children = crossover(parents, opts)
      children ++ leftover
      |> mutation(opts)
      |> evolve(problem, generation+1, opts)
    end
  end
end
