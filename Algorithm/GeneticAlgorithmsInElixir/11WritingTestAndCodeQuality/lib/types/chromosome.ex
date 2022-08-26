defmodule Types.Chromosome do
  @type t :: %__MODULE__{
          genes: Enum.t(),
          size: integer(),
          fitness: number(),
          age: integer()
        }

  @enforce_keys :genes
  defstruct [
    :genes,
    id: Base.encode16(:crypto.strong_rand_bytes(64)),
    size: 0,
    fitness: 0,
    age: 0
  ]

  defimpl String.Chars, for: __MODULE__ do
    def to_string(c), do: c.id
  end
end
