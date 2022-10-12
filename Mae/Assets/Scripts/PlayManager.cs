using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;


public class PlayManager : MonoBehaviour
{
    public Text timer;
    public Text bullet;
    public Text end_text;
    

    public static int b_cnt = 5;
    public static int r_cnt = 3;
    private float period = 0;

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        

        if (b_cnt == 0 || r_cnt == 0)
        {
            if (PlayManager.r_cnt == 0) end_text.text = "성 공 !";
            else end_text.text = "실 패 !";
            r_cnt = 3;
            b_cnt = 5;
            GameManager.state = PlayState.End;
            period = 0;

            
        }
        bullet.text = b_cnt.ToString();
        if (GameManager.state == PlayState.Play)
        {
            period += Time.deltaTime;
            timer.text = string.Format("{0:0.00}", period);
            if (Input.GetMouseButtonDown(0))
            {
                PlayManager.b_cnt -= 1;
            }
        }
    }
}
