import { Badge } from "./ui/badge";

function Todo({
  descTodo,
  id,
  done,
  onDelete,
  onDone,
}: {
  descTodo: string;
  id:number;
  done: boolean | undefined;
  onDelete: (id: number) => void;
  onDone: (id: number) => void;
}) {
  return (
    <section className="form w-full bg-gray-700/95 my-[1px] p-4 flex justify-between">
      <div>
        <h3
          className={`scroll-m-20 text-2xl font-semibold tracking-wider ${
            done ? "line-through text-gray-400" : ""
          }`}
        >
          {descTodo}
        </h3>
      </div>
      <div>
        {!done && (
          <Badge
            className=" bg-white hover:bg-white text-blue-500 border border-blue-500 cursor-pointer"
            onClick={() => onDone(id)}
          >
            Completed
          </Badge>
        )}
        <Badge
          className="ml-2 bg-white hover:bg-white text-red-500 border border-red-500 cursor-pointer"
          onClick={() => onDelete(id)}
        >
          Delete
        </Badge>
      </div>
    </section>
  );
}

export default Todo;
