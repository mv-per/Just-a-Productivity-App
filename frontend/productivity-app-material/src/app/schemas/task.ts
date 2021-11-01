export interface Task {
    id?: number; //? declares it's not required
    name: string;
    day: Date;
    description:string
    reminder: boolean;
}