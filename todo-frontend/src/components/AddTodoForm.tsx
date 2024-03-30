"use client";

import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";

import { Button } from "@/components/ui/button";
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form";
import { Input } from "@/components/ui/input";
import { describe } from "node:test";

const formSchema = z.object({
  descTodo: z
    .string()
    .min(4, {
      message: "Description must have at least 4 characters.",
    })
    .max(25, {
      message: "Description must have less than 20 characters.",
    }),
});

export default function AddTodoForm({
  onAdd,
}: {
  onAdd: (descTodo: string) => void;
}) {
  function onSubmit(values: z.infer<typeof formSchema>) {
    onAdd(values.descTodo);
    form.reset();
  }
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      descTodo: "",
    },
  });

  return (
    <Form {...form}>
      <form
        onSubmit={form.handleSubmit(onSubmit)}
        className="space-y-8 flex justify-between"
      >
        <FormField
          control={form.control}
          name="descTodo"
          render={({ field }) => (
            <FormItem className="flex flex-col w-4/5">
              <FormLabel className="self-start tracking-wider text-md font-bold">
                Describe todo
              </FormLabel>
              <FormControl>
                <Input width={"full"} className="text-black" {...field} />
              </FormControl>

              <FormMessage className="self-start" />
            </FormItem>
          )}
        />
        <Button type="submit">Add Todo</Button>
      </form>
    </Form>
  );
}
