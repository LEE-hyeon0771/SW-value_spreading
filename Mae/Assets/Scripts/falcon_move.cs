using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class falcon_move : MonoBehaviour
{
    float s_point = 1;
    private float x_pos = 0;
    private float y_pos = 0;
    private float period = 0;

    public GameObject falcon;

    Vector2 curr_pos;
    Quaternion curr_rot;
    bool isturn = false;
    private Vector2 initial_pos;

    // Start is called before the first frame update
    void Start()
    {
        s_point = Random.Range(1, 6);
        period = 0;
        curr_pos = falcon.transform.position;
        initial_pos = falcon.transform.position;
    }

    // Update is called once per frame
    void Update()
    {
        period += Time.deltaTime;
        x_pos = Mathf.Cos(period);
        y_pos = Mathf.Sin(s_point * period);
        curr_pos.x = initial_pos.x + x_pos * 250;
        curr_pos.y = initial_pos.y + y_pos * 100;
        falcon.transform.position = curr_pos;

        if (!isturn)
        {
            if (x_pos > 0.95)
            {
                isturn = true;
                curr_rot.y = curr_rot.y + 180;
                falcon.transform.rotation = curr_rot;
            }
        }
        else
        {
            if (x_pos < -0.95) { 
                isturn = false;
                curr_rot.y = curr_rot.y - 180;
                falcon.transform.rotation = curr_rot;
            }

        }
    }
}
