export interface GameResponse {
  game_id: string;
  board: any[][];
  current_turn: string;
  is_finished: boolean;
  winner: string | null;
}