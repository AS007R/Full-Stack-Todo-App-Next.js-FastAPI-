"use client";
import AddTodoForm from "@/components/AddTodoForm";
import Todo from "@/components/Todo";
import { useEffect, useState } from "react";

type TodoType = {
  title: string;
  id: number;
  done: boolean;
};

export default function Home() {
  const [allTodo, setAllTodo] = useState<TodoType[]>([]);
  let todoFind:boolean = true
  // getting all todoes from an api

  const deleteTodo = (id: number) => {
    const query = fetch(`http://localhost:8000/todos/${id}`, {
      method: "DELETE",
    })
  };

  useEffect(() => {
    const getData = async () => {
      try {
        const res = await fetch("http://localhost:8000/todos");
        const data: TodoType[] = await res.json();

        setAllTodo(data);
        
      } catch (error) {
        throw new Error(`HTTP error! Status: ${error}`)
        todoFind = false
      }
    };

    getData();
  }, [deleteTodo]);
  const onAdd = async (descTodo: string) => {
  
    const query = await fetch("http://localhost:8000/todos", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        "title": descTodo
      }),
    });
    console.log(query);
  };


  const onDone = (id: number) => {
    const query = fetch(`http://localhost:8000/todos/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        "done": true
      }),
    })
    console.log(query);
  };

  return (
    <center className=" min-h-screen pt-14 bg-gray-300">
      <div className="bg-black h-[600px] w-[800px] rounded-3xl text-white py-6 px-20 ">
        <h1 className="scroll-m-20 text-2xl font-extrabold tracking-wide lg:text-3xl">
          My Todos
        </h1>
        <div className="form w-full bg-gray-700/95 my-4 p-4">
          <AddTodoForm onAdd={onAdd} />
        </div>
        <div className="mt-4 h-[70%] overflow-y-auto">
    
          
        {allTodo.length == 0? <h1 className="scroll-m-20 text-2xl text-red-500 font-extrabold tracking-wide ">
          Nothing to do today!
        </h1>: allTodo.map((todo) => (
            <Todo
              key={todo.id}
              id = {todo.id}
              descTodo={todo.title}
              done={todo.done}
              onDelete={deleteTodo}
              onDone={onDone}
            />
          ))}
        </div>
      </div>
    </center>
  );
}
