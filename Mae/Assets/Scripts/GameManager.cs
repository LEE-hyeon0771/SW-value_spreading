using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public enum PlayState
{
    Start, Play, End
}
public class GameManager : MonoBehaviour
{
    public static PlayState state;
    public CanvasGroup StartCanvas;
    public CanvasGroup PlayCanvas;
    public CanvasGroup EndCanvas;

    public void Start()
    {
        GameManager.state = PlayState.Start;
    }

    public void Update()
    {
        if(GameManager.state == PlayState.End)
        {
            CanvasGroupOnOff(PlayCanvas, EndCanvas);
        }
    }

    public void StartBtn()
    {
        CanvasGroupOnOff(StartCanvas, PlayCanvas);
        GameManager.state = PlayState.Play;
    }

    public void EndBtn()
    {
        GameManager.state = PlayState.Start;
        CanvasGroupOnOff(EndCanvas, StartCanvas);
    }

    public void CanvasGroupOnOff(CanvasGroup c1, CanvasGroup c2)
    {
        c1.alpha = 0;
        c1.interactable = false;
        c1.blocksRaycasts = false;

        c2.alpha = 1;
        c2.interactable = true;
        c2.blocksRaycasts = true;
    }
}
