defmodule Speller do
  @behaviour Problem
  alias Types.Chromosome

  def genotype do
    genes =
      Stream.repeatedly(fn -> Enum.random(?a..?z) end)
      |> Enum.take(20)
    %Chromosome{genes: genes, size: 20}
  end

  def fitness_function(chromosome) do
    target = "supercalifragilistic"
    guess = chromosome.genes
    String.bag_distance(target, List.to_string(guess))
  end

  def terminate?(population), do: hd(population).fitness == 1
end

soln = Genetic.run(Speller)

IO.write("\n")
IO.inspect(soln)