export interface Comment {
    id: number;
    comment_id: number;
    by: string;
    text: string;
    type: string;
    time: string;
    parent_story: number;
  }
  
  export interface Story {
    id: number;
    comments: Comment[];
    story_id: number;
    title: string;
    by: string;
    descendants: number;
    score: number;
    text: string;
    type: string;
    time: string;
    url: string;
  }