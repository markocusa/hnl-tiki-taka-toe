import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { GameService } from './services/game.service';
import { GameResponse } from './models/game.model';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  gameId: string | null = null;
  board: any[][] = [];
  selectedPlayer = "Filip Bradarić";
  currentTurn:string | null = null;
  isFinished = false;
  winner: string | null = null;
  constructor(private gameService: GameService) {}

  createGame() {
    this.gameService.createGame().subscribe((res:GameResponse) => {
      this.gameId = res.game_id;
      this.loadGame();
    });
  }

  loadGame() {
    if (!this.gameId) return;
    this.gameService.getGame(this.gameId).subscribe((res:GameResponse) => {
      this.board = res.board;
      this.currentTurn = res.current_turn;
      this.winner = res.winner;
    });
  }

  onCellClick(row: number, col: number) {
    if (!this.gameId) return;

    const cell = this.board[row][col];
    if (cell?.symbol) return;

    this.gameService.playMove({
      game_id: this.gameId,
      row,
      col,
      player_name: this.selectedPlayer
    }).subscribe(res => {
      console.log("Move result:", res);

      if (res.valid) {
        this.board = res.board;
        this.currentTurn = res.current_turn;
        this.isFinished = res.is_finished;
        this.winner = res.winner;
      } else {
        alert(res.reason);
      }
    });
  }
}