export interface Task {
    id?: number; //? declares it's not required
    text: string;
    day: string;
    reminder: boolean;
}